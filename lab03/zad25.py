class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Nowe saldo: {self.balance:.2f}')
        elif amount > self.balance:
            print("Niewystarczające środki na koncie.")
        else:
            print("Kwota wypłaty musi być większa od zera.")

konto = BankAccount(100)
konto.deposit(50)
konto.withdraw(30)
konto.withdraw(150)