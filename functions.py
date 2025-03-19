def add_income(budget_data, amount, description):
    """מוסיף הכנסה לתקציב ומעדכן את היתרה"""
    budget_data["transactions"].append({"type": "income", "amount": amount, "description": description})
    budget_data["balance"] += amount
    return budget_data  # מחזיר את הנתונים המעודכנים


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