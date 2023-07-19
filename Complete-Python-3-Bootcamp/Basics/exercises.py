for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)


st = 'Create a list of the first letters of every word in this string'

list = [a[0] for a in st.split()]
print(list)
