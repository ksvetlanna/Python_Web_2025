# ООП Class

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Депозит пополнен на сумму {amount}.')
        else:
            print(f'Нельзя вносить отрицательную сумму на депозит.')

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            print(f'С депозит снята сумма {amount}.')
        else:
            print(f'Не хватает средств. Овердрафт не доступен.')

client1 = BankAccount('John')
client1.deposit(500)
client1.withdraw(400)
print('Остаток:', client1.get_balance())