from Bank.bank import Bank
from accs.saving_account import SavingAccount
from accs.checking_account import CheckingAccount
from Client.Client import Client

bank = Bank()
c1 = Client('Vinicius', 19)
c2 = Client('João', 20)
c3 = Client('Jean', 35)
acc1 = CheckingAccount(1111, 22221, 10)
acc2 = SavingAccount(1111, 22221, 10)
acc3 = CheckingAccount(1411, 22221, 10)
c1.insert_account(acc1)
c2.insert_account(acc2)
c3.insert_account(acc3)
bank.insert_client(c1)
bank.insert_acc(acc1)

if bank.validate(c1):
    c1._account.deposit(10)
    c1._account.withdraw(10)
else:
    print('Cliente não autenticado')
print()
if bank.validate(c3):
    c3._account.deposit(10)
    c3._account.withdraw(10000)
else:
    print('Cliente não autenticado')
