coun_file = open('coun.txt', 'r')
print(coun_file.readable())
#print(coun_file.readline())

countries = coun_file.readlines()
print(countries[1])
coun_file.close()

writ = open('coun.txt', 'w')
writ.write('Hello \nbanana \nstraw')

writ = open('coun_new.txt', 'w')
writ.write('Hello new file')

writ = open('coun_new.txt', 'a')
writ.write('\nHello my new line 2')

py_file = open('py_file.py', 'w')
py_file.write('print(\'woww\')')


