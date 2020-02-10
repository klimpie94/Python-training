"""
In this exercise you're going to create a bank account class with some typical functionality.​

Your bank account class should have/be able to:​

    1. The class declaration​

    2. Data about the customer such as their first name, last name, account number, and balance.​

    3. The ability to make a deposit.​

    4. The ability to make a withdrawal.​ (With a limit of 500)

    5. The ability to see the most recent transaction.
"""

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