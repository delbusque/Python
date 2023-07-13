def has_3_3(list_ints):
    for i in range(0, len(list_ints)-1):
        if list_ints[i] == 3 and list_ints[i+1] == 3:
            return True

    return False


has_3_3([1, 3, 3])


def paper_doll(strin):
    result = ''
    for lett in strin:
        result += lett * 3


paper_doll('asd')


def black_jack(a, b, c):
    curr = a + b + c

    if curr <= 21:
        print(curr)
    elif curr > 21 and (a == 11 or b == 11 or c == 11):
        curr -= 10
        if curr > 21:
            print('BUST')
        else:
            print(curr)
    elif curr > 21:
        print('BUST')


black_jack(9, 9, 9)


def summer_69(arr):
    result = 0
    flag = True

    for num in arr:
        while flag:
            if num != 6:
                result += num
                break
            else:
                flag = False

        while not flag:
            if num != 9:
                break
            else:
                flag = True

    print(result)


summer_69([2, 1, 6, 9, 11])
