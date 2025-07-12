monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income - monthly_expenses)
print(f"Your monthly savings are: ${monthly_savings:.0f}")
annual_rate = 0.05
def projected_savings(monthly_savings):
    annual_savings = monthly_savings * 12
    interest = annual_savings * annual_rate
    projected_savings = annual_savings + interest
    return projected_savings
annual_savings = float(monthly_savings * 12)
interest = float(annual_savings * annual_rate)
projected_savings = float(annual_savings + interest)
print(f'Projected savings after one year, with interest, is: ${projected_savings:.0f}')