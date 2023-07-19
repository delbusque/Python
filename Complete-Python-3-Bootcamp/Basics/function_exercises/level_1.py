def func(name):
    result = ''
    result += name[:3].capitalize()
    result += name[3:].capitalize()

    print(result)


func('macdonalds')


def reversed(sentence):
    rev = sentence.split()
    rev.reverse()
    result = []
    count = 0

    for word in rev:
        if count == 0:
            result.append(word.capitalize())
            count += 1
        else:
            result.append(word.lower())

    print(' '.join(result))


reversed('We Are GeAdy')

myl = ['a', 'b', 'c']

print(myl[::-1])
