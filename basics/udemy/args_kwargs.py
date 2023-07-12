def myfunc(*args):
    print(sum(args) * 0.05)


myfunc(100, 200, 200, 500)


def get_fruit(**kwargs):
    for item in kwargs:
        if item == 'fruit':
            print(f'My fav fruit is {kwargs[item]}')
        else:
            pass


get_fruit(fruit='apple', dog='mango')


def get_fr(*args, **kwargs):
    su = sum(args)

    for item in kwargs:
        if item == 'fruit' and su == 100:
            print(f'{su} % my fav fruit is {kwargs[item]}')
        else:
            pass
    print(args)
    print(kwargs)


get_fr(1, 2, 97, fruit='apple', dog='mango')
