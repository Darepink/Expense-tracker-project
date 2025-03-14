# List to store all expenses
expenses = []

# Function to add a new expense
def add_expense():
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    amount = input("Enter the amount spent: ")
    date = input("Enter the date (YYYY-MM-DD): ")

    # Create a dictionary to store the expense details
    expense = {
        "category": category,
        "amount": float(amount),
        "date": date
    }
    
    # Add the expense to the list
    expenses.append(expense)
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
    else:
        print("All Expenses:")
        for i in range(len(expenses)):
            print(f"{i + 1}. Category: {expenses[i]['category']}, Amount: ${expenses[i]['amount']:.2f}, Date: {expenses[i]['date']}")
        print()

# Function to filter expenses by category
def filter_expenses():
    category = input("Enter the category to filter by: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}")
            found = True
    
    if not found:
        print("No expenses found for this category.\n")

# Function to calculate total expenses
def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: ${total:.2f}\n")

# Function to delete a specific expense
def delete_expense():
    view_expenses()
    if len(expenses) == 0:
        return  # No expenses to delete

    choice = input("Enter the number of the expense to delete: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"Deleted expense: {deleted['category']} of ${deleted['amount']:.2f}.\n")
        else:
            print("Invalid expense number.\n")
    else:
        print("Invalid input. Please enter a valid number.\n")

# Main menu loop
def main():
    while True:
        print("Expense Tracker Menu")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Filter expenses by category")
        print("4. Calculate total expenses")
        print("5. Delete an expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
