"""
In this exercise you're going to create a bank account class with some typical functionality.​

Your bank account class should have/be able to:​

    1. The class declaration​

    2. Data about the customer such as their first name, last name, account number, and balance.​

    3. The ability to make a deposit.​

    4. The ability to make a withdrawal.​ (With a limit of 500)

    5. The ability to see the most recent transaction.
"""

class BankAccount:

    """A class example in python that models a bank account"""

    def __init__(self, first_name, last_name, account_num, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount

    def withdrawal(self, amount, limit=500):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' '${}. \
            \nYour withdrawal limit is {}'.format(amount, self.balance, limit)
    
    def recent_transactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()
    

a = BankAccount('Anis', 'Boudih', 3628902828)
print('first name =', a.first_name)
print('last name =', a.last_name)
print('account number =', a.account_num)
print('account balance =', a.balance)
print('deposit =', a.deposit(20))
print('recent transaction is:', a.recent_transactions())
print('account balance =', a.balance)
print('withdrawal =', a.withdrawal(50))
print('recent transaction is =', a.recent_transactions())
print('account balance =', a.balance)
print('deposit =', a.deposit(500))
print('withdrawal =', a.withdrawal(891))
print('recent transaction is =', a.recent_transactions())
print('withdrawal =', a.withdrawal(49))
