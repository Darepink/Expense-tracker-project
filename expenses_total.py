expenses = {}



def calculate_total():
    total = sum(expenses.values())
    print(f"Total: ${total:.2f}")

def delete_expense():
    expense_id = input("Enter ID to delete: ")
    if expense_id in expenses:
        expenses[expense_id] = None
        print("Marked as deleted.")
    else:
        print("ID not found.")

def main():
    while True:
        print(" Total\n1. Delete expense\n2. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()