from bank_accounts import *

GGM = BankAccount(1000, "GGM") # Class first letter starts with caps
Milan = BankAccount(500, "Milan")

GGM.get_balance()
GGM.deposit(700)
GGM.withdraw(2000)
GGM.withdraw(200)
print('')
GGM.transfer(700, Milan)

Fidel = InterestRewardAcct(1000, "Fidel")
Milan_07 = SavingsAcct(5000, "Milan")
Fidel.get_balance()
Fidel.deposit(70)
print('')
Milan_07.get_balance()
Milan_07.withdraw(750)
Milan_07.transfer(700, Fidel)


