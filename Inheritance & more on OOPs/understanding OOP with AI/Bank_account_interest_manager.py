class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    @property
    def interest_amount(self):
        return (self.balance * self.interest_rate) / 100
    
    @interest_amount.setter
    def interest_amount(self, value):
        self.interest_rate = (value * 100)/ self.balance

b = BankAccount(1000, 5)
print(b.interest_amount)
b.interest_amount = 75
print(b.interest_rate)