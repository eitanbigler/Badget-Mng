### Interactive functions ###
def get_valid_float(prompt):
    while True:
        try:
            if prompt:
                prompt=prompt.strip()+": "
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a value greater than 0.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.\n")

def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Invalid input, the string cannot be empty.\n")

def get_valid_y_n(prompt):
    value = get_valid_string(prompt)

    while True:
        if value.lower() not in ['n','y']:
            value = get_valid_string("Y/n? ")
        else:
            break

    return value.lower() == 'y'


def add_income(budget_data):
    """מוסיף הכנסה לתקציב ומעדכן את היתרה"""
    while True:
        amount = get_valid_float("Enter income amount: ")
        description = get_valid_string("Enter description: ")

        budget_data["transactions"].append({"type": "income", "amount": amount, "description": description})
        budget_data["balance"] += amount

        if not get_valid_y_n("Do you wish to insert another income? "):
            return budget_data


def add_expense(budget_data, amount, description):
    """מוסיף הוצאה לתקציב ומעדכן את היתרה"""
    budget_data["transactions"].append({"type": "expense", "amount": amount, "description": description})
    budget_data["balance"] -= amount
    return budget_data  # מחזיר את הנתונים המעודכנים


def show_balance(budget_data):
    """מדפיס את היתרה הנוכחית"""
    print(f"Current Balance: {budget_data['balance']}")


def show_transactions(budget_data):
    """מדפיס את כל העסקאות"""
    print("\nTransaction History:")
    if not budget_data["transactions"]:
        print("No transactions yet.")
    else:
        for transaction in budget_data["transactions"]:
            print(f"{transaction['type'].capitalize()}: {transaction['amount']} ({transaction['description']})")
    print("----------------------")