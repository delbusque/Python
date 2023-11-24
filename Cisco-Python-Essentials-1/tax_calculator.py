income = float(input('Income is: '))
mark = 85528

if income <= mark:
    tax = income * 0.18 - 556.02
else:
    surplus = income - mark
    tax = 14839.02 + surplus * 0.32

if tax < 0:
    tax = 0

print('The tax is:', round(tax, 0), 'thalers')
