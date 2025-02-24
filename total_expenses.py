# Dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    # Asking user to input an expense ID and amount
    expense_id = input("Enter expense ID: ")
    amount = float(input("Enter amount: $"))
    # Store the expense in the dictionary
    expenses[expense_id] = amount

# Function to calculate and display the total expenses
def calculate_total():
    # Sum the values in the expenses dictionary and display total
    print(f"Total: ${sum(expenses.values()):.2f}")

# Function to display all expenses
def view_expenses():
    # Loop through all expenses and display their IDs and amounts
    for expense_id, amount in expenses.items():
        print(f"ID: {expense_id}, Amount: ${amount:.2f}")

# Function to filter expenses by a minimum amount
def filter_expenses():
    # Ask user for a threshold value to filter expenses
    threshold = float(input("Enter amount threshold: $"))
    # Loop through expenses and display those that are greater than the threshold
    for expense_id, amount in expenses.items():
        if amount > threshold:
            print(f"ID: {expense_id}, Amount: ${amount:.2f}")

# Main function to drive the program
def main():
    # Keep showing the menu until user chooses to exit
    while True:
        # Show the menu with options
        choice = input("\n1. Add expense\n2. View expenses\n3. Calculate total\n4. Filter expenses\n5. Exit\nChoose an option: ")
        
        if choice == '1':
            add_expense()  # Call the function to add an expense
        elif choice == '2':
            view_expenses()  # Call the function to view all expenses
        elif choice == '3':
            calculate_total()  # Call the function to calculate total
        elif choice == '4':
            filter_expenses()  # Call the function to filter expenses
        elif choice == '5':
            break  # Exit the loop and end the program
        else:
            print("Invalid option.")  # If the user enters an invalid option, print a message

# Run the main function when the program starts
if __name__ == "__main__":
    main()
