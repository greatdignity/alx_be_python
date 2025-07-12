monthly_income = int(input("Enter your monthly income: "))
totalmonthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = int(monthly_income - totalmonthly_expenses)
print(f"Your monthly savings are: ${monthly_savings}")
annual_rate = 0.05
def projected_savings(monthly_savings):
    annual_savings = monthly_savings * 12
    interest = annual_savings * annual_rate
    projected_savings = annual_savings + interest
    return projected_savings
annual_savings = monthly_savings * 12
interest = annual_savings * annual_rate
projected_savings = annual_savings + interest
print(f'Projected savings after one year, with interest, is: ${projected_savings:.0f}')