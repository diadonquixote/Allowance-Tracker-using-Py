import json


DATA_FILE = "datatracker.json"


def display_menu():
    print("\n=== Allowance Tracker ===")
    print("1. Add Allowance")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def save_data(allowances, expenses):
    data = {
        "allowances": allowances,
        "expenses": expenses
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("allowances", []), data.get("expenses", [])
    except FileNotFoundError:
        return [], []
    except json.JSONDecodeError:
        print("Warning: Data file is corrupted. Starting with empty records.")
        return [], []


def add_allowance(allowances, expenses):
    amount = get_positive_float("Enter allowance amount: ₱")
    description = input("Enter allowance source (Mommy, Papa, Work, etc.): ").strip()

    allowances.append({
        "amount": amount,
        "description": description
    })

    save_data(allowances, expenses)
    print(f"Added allowance of ₱{amount:.2f} from {description}.")


def add_expense(expenses, allowances):
    amount = get_positive_float("Enter expense amount: ₱")
    description = input("Enter expense category (Cafe, School, Transpo, etc.): ").strip()

    expenses.append({
        "amount": amount,
        "description": description
    })

    save_data(allowances, expenses)
    print(f"Added expense of ₱{amount:.2f} for {description}.")


def view_summary(allowances, expenses):
    total_allowance = sum(item["amount"] for item in allowances)
    total_expenses = sum(item["amount"] for item in expenses)
    balance = total_allowance - total_expenses

    print("\n=== Summary ===")
    print(f"Total Allowance: ₱{total_allowance:.2f}")
    print(f"Total Expenses: ₱{total_expenses:.2f}")
    print(f"Balance: ₱{balance:.2f}")


def main():
    allowances, expenses = load_data()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_allowance(allowances, expenses)
        elif choice == "2":
            add_expense(expenses, allowances)
        elif choice == "3":
            view_summary(allowances, expenses)
        elif choice == "4":
            print("magtipid na pls pu T^T")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()