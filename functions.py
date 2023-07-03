def greeting(name, age, num1, num2):
    print('Hello. My name is', name+'. I am', str(age) + '.')
    return num1 + num2


age = input('Enter your age: ')

num1 = int(input('Num1: '))
num2 = int(input())

num = greeting('Johny', age, num1, num2)

print(num)
