import os

def display_menu():
    print("Allowance Tracker")
    print("1. Add Allowance")
    print("2. Add Expense")
    print("3. Exit")

def add_allowance(allowance):
    amount = float(input("Enter allowance amount: "))
    description = input("Enter allowance source (Mommy, Papa, Work, etc.): ")
    allowance.append({"amount": amount, "description": description})
    print(f"Added allowance of ₱{amount} from {description}.")

def add_expense(expenses, allowance):
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense category (Cafe, School, Transpo, etc.): ")
    expenses.append({"amount": amount, "description": description})
    print(f"Added expense of ₱{amount} for {description}.")
    total_allowance = sum(item['amount'] for item in allowance)
    total_expenses = sum(item['amount'] for item in expenses)
    balance = total_allowance - total_expenses
    print(f"\nTotal Allowance: ₱{total_allowance}")
    print(f"Total Expenses: ₱{total_expenses}")
    print(f"Balance: ₱{balance}\n")

def main():
    allowance = []
    expenses = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_allowance(allowance)
        elif choice == "2":
            add_expense(expenses, allowance)
        elif choice == "3":
            print("magtipid na pls pu T^T")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
