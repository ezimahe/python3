# expenses = [10.56, 23, 22.90, 11.13, 6, 8, 9]
# total = sum(expenses)
# print('You spent $', total, ' on lunch this week.', sep = '')

# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("Enter an expense:")))

# total = sum(expenses)

# print('You spent $', total, ' on lunch this week.', sep = '')
# print(expenses)


total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print('You spent $', total, ' on lunch this week.', sep = '')
print(expenses)