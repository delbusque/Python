new_list = [letter for letter in 'boom']

print(new_list)

evens = [int(x/2) for x in range(0,10,2)]
odds = [x for x in range(10,20) if x % 2 != 0]

print(evens)
print(odds)

kilometers = [11, 102, 3240]
miles = [round(km * 1.61, 2) for km in kilometers]

print(miles)

list_5 = [x*y for x in [1,2,3] for y in [10,20,30]]
print(list_5)