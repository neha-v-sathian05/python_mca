class BankAccount:

    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)


account1 = BankAccount(101, "Anu", "Savings", 5000)
account2 = BankAccount(102, "Rahul", "Current", 8000)

account1.display()
account1.deposit(2000)
account1.withdraw(1000)
account1.display()

account2.display()
account2.deposit(3000)
account2.withdraw(2000)
account2.display()