import json
from datetime import datetime
from collections import defaultdict


# File to store expenses
FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses(filename=FILE_NAME):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading data file. Starting with empty data.")
        return []


# Save expenses to file
def save_expenses(expenses, filename=FILE_NAME):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    try:
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        amount = float(input("Enter the amount spent: ").strip())
        category = input("Enter the category (e.g., food, transport): ").strip().lower()
        description = input("Enter a brief description: ").strip()

        expenses.append({"date": date, "amount": amount, "category": category, "description": description})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please check the date or amount.")


# View expense summaries by category
def summarize_by_category(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]

    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f" - {category.capitalize()}: ${total:.2f}")


# View monthly expense summary
def summarize_monthly(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    month = input("Enter the month (YYYY-MM): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")  # Validate month format
        monthly_total = sum(
            expense["amount"] for expense in expenses if expense["date"].startswith(month)
        )
        print(f"\nTotal expenses for {month}: ${monthly_total:.2f}")
    except ValueError:
        print("Invalid month format. Please use YYYY-MM.")


# Main menu
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Summary by Category")
        print("3. View Monthly Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            summarize_by_category(expenses)
        elif choice == "3":
            summarize_monthly(expenses)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point
if __name__ == "__main__":
    main()