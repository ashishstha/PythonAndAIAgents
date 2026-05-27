#!/usr/bin/python3

class myClass:
    def __init__(self):
        self.__private="Ashish"
        self.name="Shrestha"
    def getPrivate(self):
        return self.__private
    def __showPrivate(self):
        print(self.__private)

obj = myClass()
#print(obj.__private) #This will raise an error because __private is a private variable and cannot be accessed directly from outside the class.
print(obj._myClass__private) #This will work because we can access the private variable using the name mangling syntax _ClassName__variableName.
print(obj.getPrivate()) #This will work because getPrivate() is a public method that can access the private variable __private and return its value.
print(obj.name) #This will work because name is a public variable and can be accessed directly from outside the class.  

print(obj._myClass__showPrivate()) #This will work because we can access the private method using the name mangling syntax _ClassName__methodName.


#Real time example of private variable and method
class BankAccount:
    def __init__(self,account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")  

    def withdraw(self, amount):
        if(amount > 0) and (amount <=self.__balance):
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.") 

account = BankAccount("123456789", 1000)
print(account.get_balance()) # This will work because get_balance() is a public method that can access the private variable __balance and return its value.
account.deposit(500) # This will work because deposit() is a public method that can access
account.withdraw(200) # This will work because withdraw() is a public method that can access the private variable __balance and update its value.
account.__balance = 1000000 # This will not change the actual balance because __balance is a private variable and cannot be accessed directly from outside the class. It will create a new variable __balance in the instance's namespace, but it will not affect the private variable __balance defined in the class.
print(account.get_balance()) # This will still return 1300 because the private variable __balance