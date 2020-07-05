"""
Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""
class Account():
    def __init__(self,owner,balance = 0):
        
        self.owner = owner    
        self.balance = balance
        
        
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the bslsnce")
        
    def withdraw(self,wd_amt):
        
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("withdraw accepted !!!")
        
        else:
            print("sorry not enough money !!!")
            
    def __str__(self):
        return f"Owner:{self.owner} \nBalance:{self.balance}"

a = Account("Ram" , 1000)
a.owner
a.balance
print(a)


a.deposit(500)
print(a)
a.withdraw(1400)