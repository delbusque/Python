import math

name = 'Todd'
num1 = 100.2
num = round(num1)

numSqrt = math.sqrt(num)

print('Hello', name.upper()+'.\nHow are you ?')
print('I`m', int(numSqrt) * 10, '% !!!')

flag = name.isupper()

print(flag)

nick = input('nickname: ')
age = int(input('age: '))

print(nick, 'is', age)

age = 22

print(nick, 'is', age)
