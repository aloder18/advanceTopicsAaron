class BankAccount:

    def __init__(self, number, name):
        self.balance = 0
        self.number = number
        self.owner = name

    def deposit(self,amount):
        self.balance += amount
        print amount, "dollars have been deposited."
        print self.balance, "dollars is your new balance."

    def withdraw(self,amount):
        self.balance -= amount
        print amount, "dollars have been withdrawn."
        print self.balance, "dollars is your new balance."

    def check(self):
        print self.balance, "dollars is your current balance."

newAccount = BankAccount(1,"Aaron")
newAccount.deposit(200)
newAccount.check()
newAccount.withdraw(10)
newAccount.check()
