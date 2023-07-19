def spy_game(arr):
    count_zero = 0
    index = 0

    while count_zero < 2:
        for i in arr:
            index += 1
            if i == 0:
                count_zero += 1

    for i in arr[index-1:]:
        if i == 7:
            print('007')
            return

    print(False)


def spy_game_2(arr):
    code = [0, 0, 7, 'x']
    for n in arr:
        if n == code[0]:
            code.pop(0)
    print(len(code) == 1)


spy_game_2([1, 7, 2, 0, 0, 5, 7])


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
