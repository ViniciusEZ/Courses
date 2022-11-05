from account.saving_account import SavingAccount
from account.checking_account import CheckingAccount

BA = SavingAccount('Itau', '1234', 345)

BA.detail()
BA.withdraw(100)
BA.deposit(1000)
print('*'*20)
CA = CheckingAccount('Santander', 1246, 200, 200)
CA.detail()
CA.withdraw(400)
CA.deposit(500)
CA.withdraw(1000)
