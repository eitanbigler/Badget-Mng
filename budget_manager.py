from functions import * # מייבא את הפונקציות מקובץ py

# יצירת מבנה הנתונים
def main(data):
    while True:
        print("\nBudget Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            data = add_income(data)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            data = add_expense(data, amount, description)

        elif choice == "3":
            show_balance(data)

        elif choice == "4":
            show_transactions(data)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

    return data  # מחזיר את המידע המעודכן


if __name__ == "__main__":
    budget_data = {"balance": 0, "transactions": []}  # יצירת מבנה הנתונים
    budget_data = main(budget_data)  # קריאה לפונקציה עם הנתונים
