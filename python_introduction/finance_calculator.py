monthly_income =int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

def cal (monthly_income, monthly_expenses):
    Monthly_Savings = monthly_income - monthly_expenses
    return Monthly_Savings
Monthly_Savings =cal(monthly_income, monthly_expenses)
annual_savings = (Monthly_Savings) * 12
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)


print(f"Your monthly savings are {Monthly_Savings}.")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")
