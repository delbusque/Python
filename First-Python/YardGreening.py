area = float(input())

total_price = area * 7.61
discount = float(format(total_price * 0.18, '.2f'))
price_after_discount = float(format(total_price - discount, '.2f'))

print(f'The final price is: {price_after_discount} lv.')
print(f'The discount is: {discount} lv.')