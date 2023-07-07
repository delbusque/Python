listing = [1, 22, 333, ['boom', 'crash']]
listing_2 = [[1,2,3], ['boom', 'crash']]

print(listing_2[1][1])

for list in listing_2:
    for x in list:
        print (x)


for x in range(10,15):
    print(x)
    if x == 13:
        break

i = 1
while i <= 5:
    print(i)
    i += 1