class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self,cash_withdrawn):
        if(self.__balance>=cash_withdrawn):
            print(f"{cash_withdrawn} has been withdrawn.")
            self.__balance -= cash_withdrawn
        else:
            print(f"Bank balance is too low for cash withdrawl. Balance is: {self.__balance}")
    def get_balance(self):
        return self.__balance
    
user = BankAccount(10000)
user.deposit(5000)
user.withdraw(15000)
print(user.get_balance())
user.withdraw(15000)

