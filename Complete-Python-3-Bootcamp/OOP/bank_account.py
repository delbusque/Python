class Account():

    __balance = 0

    def __init__(self,owner):
        self.owner = owner
        print(f'{self.owner}\'s bank account balance is ${self.__balance}')

    def deposit(self, ammount):
        self.__balance += ammount
        print(f'{self.owner}\' bank account new balance is ${self.__balance}')


    def withdraw(self, ammount):
        if ammount <= self.__balance:
            self.__balance -= ammount
            print(f'After withdraw of ${ammount} {self.owner}\' bank account new balance is ${self.__balance}')
        else:
            print(f'${ammount} is more than ${self.__balance} and can not withdraw it')

    def __str__(self):
        return f'Owner: {self.owner}\nBalance: {self.__balance}'

jons = Account('John')

jons.withdraw(100)
jons.deposit(1000)
jons.withdraw(100)

print(str(jons))


