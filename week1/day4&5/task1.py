class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amt):
        self.__balance += amt
        
    def withdraw(self, amt):
        self.__balance -= amt

    def get_balance(self):
        return self.__balance

b = BankAccount(1000)
print(b.get_balance()) 
b.deposit(500)
print(b.get_balance()) 
b.withdraw(1500)
print(b.get_balance())  # 1500
