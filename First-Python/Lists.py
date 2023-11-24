my_list = [1, 2, 3, 4]
just_list = ['this is a string', 100, 2.74]
print(len(my_list))
print(len(just_list))

x = my_list[0] + just_list[1]
print(x)
print(my_list[:1])
print(my_list[1:])

y = my_list + just_list
print(y)

y[3] = 200
print(y)

y.append(300)
print(y)
y.pop()
item = y.pop(-1)
print(item)
print(y)

newlist = ['c', 'd', 'b', 'a']
newlist.sort()
print(newlist)
z = [2, 4, 4, 1, 3]
z.sort()
u = z
u.reverse()
print(u)

u.remove(4)
print(u)
u.pop(0)
print(u)

u.append("The End")
print(u)
u.remove('The End')
print(u)
u.pop()
print(u)

nested = [1, 2, [3, 4], 'Name', 'Age']
index = nested[2]
nested_index = index[1]
print(index)
print(nested_index)

x = {'dog': [12, 13, 22], 'cat': [33, 33, 22]}
print(x['cat'][2])
