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
