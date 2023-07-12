def myfunc(*args):
    my_list = []

    for a in args:
        if a % 2 == 0:
            my_list.append(a)

    return my_list


def myfunc_2(strin):
    count = 0
    my_strin = ''

    for let in strin:
        if count % 2 == 0:
            my_strin += let.upper()
            count += 1
        else:
            my_strin += let.lower()
            count += 1

    return my_strin
