print("Welcome to the Personal Expense Tracker! Created by: [Bhaskar]")
print("This tool will help you track your monthly expenses and manage your finances effectively.")
Salary=input("Enter your monthly salary: ")
Salary_= float(Salary)
Num = int(input("Enter the number of expenses you want to track: "))

Expenses = []
for i in range(Num):
    Expenses.append(input("Enter the name of the expense: "))

Amount = []
for i in range(Num):
    Amount.append(float(input("Enter the amount for the Expense of  {}: ".format(Expenses[i]))))

print("📊 EXPENSE SUMMARY")

Expense_Data = list(zip(Expenses, Amount))
print("Your Expenses and their corresponding amounts are: ")
for expense, amount in Expense_Data:
    print("{}: {}".format(expense, amount))

print("💰 Your monthly salary is: ", Salary_)
Total = sum(Amount)
print("💸Total expenses: ", Total)

Savings = Salary_ - Total
print("💵 Savings: ", Savings)
if Savings < 0:
    print("You have overspent by: ", abs(Savings))
elif Savings == 0:
    print("You Spent Whole Salary this month.")
else:
    print("This Month You Saved:", Savings)


Percent = (Savings / Salary_) * 100
print("📈You saved ", Percent, "% of your salary this month.")

Spend_most = max(Amount)
Index = Amount.index(Spend_most)
print("🔥 Your highest expense is: ", Expenses[Index], "with an amount of: ", Spend_most)
if Savings < 0:
    print("You need to cut down on your expenses, especially on: ", Expenses[Index])
else:
    if Salary_ % 20 <= Savings:
        print("You are on track to save a good portion of your salary this month.")
    else:
        print("You need to be more careful with your expenses this month.")