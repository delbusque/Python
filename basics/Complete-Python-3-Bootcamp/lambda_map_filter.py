def func(strin):
    if len(strin) % 2 == 0:
        return 'EVEN'
    else:
        return strin[0]


my_list = ['hello', 'Andy', 'London']

result = map(func, my_list)

for a in result:
    print(a)


def evens(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6, 7, 9]

even_nums = list(filter(evens, my_nums))

print(even_nums)


odds = list(filter(lambda n: n % 2 != 0, my_nums))
print(odds)

multiplies = list(map(lambda a: a * 2, my_nums))
print(multiplies)

reversed = list(map(lambda name: name[::-1], my_list))
print(reversed)
