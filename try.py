try:
    x = int(input('Enter me: '))
    print(x)
except:
    print('Not an integer')
else:
    print('Nothing went wrong')
finally:
    print('Finished')