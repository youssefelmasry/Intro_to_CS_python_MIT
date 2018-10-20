#Paying Debt off in a Year - balance

monthly_interest_rate = annualInterestRate/12.0
for i in range(12):
	minimum_monthly_payment = monthlyPaymentRate*balance
	monthly_unpaid_balance = balance - minimum_monthly_payment
	balance = monthly_unpaid_balance + (monthly_interest_rate*monthly_unpaid_balance)
print("%.2f"%balance)	