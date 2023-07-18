nums = (1, 3, 44)
strings = ('my', 'heart', 'uk')
tup = (1, True, 'big')

constr = tuple((1, False, 'Japan', 3.14))

print(constr[3])
print(len(tup))

def players():

    player_1 = ''
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input('Player 1 select "X" or "O": ')

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    return (player_1, player_2)

player_1, player_2 = players() # unpacking tuple

print(player_1)
print(player_2)