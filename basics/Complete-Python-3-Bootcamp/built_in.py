x = range(1,10,3)
y = list(x)

print(y)


index = 0
word_index = 0

strin = 'abcde'
word = 'magic'

for letter in strin:
    print('At index {} letter is {}'.format(index, letter))
    index += 1

for letter in word:
    print(word[word_index])
    word_index += 1


lis = ['apple', 'banana', 'milk']

print(list(enumerate(lis,1)))

for index, item in enumerate(lis):
    print(index)
    print(item)

lis_2 = [1,2,3,4,5,6]
lis_3 = [10,20,'am',4]

y = zip(lis_2, lis, lis_3)

for z,m,v in y:
    print(v,m)

yes = 'm' in lis[2]
print(yes)

d = {'key': 123}

is_key = 'key' in d
is_value = 123 in d.values()

print(is_key)
print(is_value)

from random import shuffle, randint

shuffle(lis_2)

print(lis_2)
print(randint(1,10))
