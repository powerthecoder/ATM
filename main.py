import time
import os
import sys
import json



class Main():
    def __init__(self):
        try:
            with open("balance.json", "r") as f:
                data = json.load(f)
            ttl = data['total']
            self.total = ttl
        except Exception as e:
            print(f"[ERROR] > {e}")
        option = int(input("Option > "))
        
        if (option == 1):
            x = 0
            while (x != 1):
                amount = float(input("Amount to deposit $"))
                if (amount > 0):
                    try:
                        print(f"Depositing ${amount}")
                        self.Deposit(amount)
                        x += 1
                    except Exception as e:
                        print(f"[ERROR] > {e}")
                else:
                    print(f"Can not deposit ${amount}")
        
        elif (option == 2):
            x = 0
            while (x != 1):
                amount = float(input("Amount to withdraw $"))
                if (amount > 0):
                    try:
                        with open("balance.json", "r") as f:
                            data = json.load(f)
                        total = data['total']
                        if (amount < float(total)):
                            print(f"Withdrawing ${amount}")
                            self.Withdraw(amount)
                            x += 1
                        else:
                            print(f"Not enough funds in account to withdraw ${amount}")
                    except Exception as e:
                        print(f"[ERROR] > {e}")
                else:
                    print(f"Can not withdraw ${amount}")

        elif (option == 3):
            self.Balance()
        
        else:
            print("Unknown Argument...")
            print("Shutting Down")
            time.sleep(1)
            sys.exit()
    
    def Deposit(self, amount):
        try:
            with open("balance.json", "r") as f:
                data = json.load(f)
            total = data['total']
            new_total = float(total) + float(amount)
            print(f"New Total: ${new_total}")
            data['total'] = float(new_total)
            with open("balance.json", "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"[ERROR] > {e}")

    def Withdraw(self, amount):
        try:
            with open("balance.json", "r") as f:
                data = json.load(f)
            total = data['total']
            new_total = float(total) - float(amount)
            print(f"New Total: ${new_total}")
            data['total'] = float(new_total)
            with open("balance.json", "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"[ERROR] > {e}")

    def Balance(self):
        try:
            with open("balance.json", "r") as f:
                data = json.load(f)
            total = data['total']
            print(f"Your Total is ${total}")
        except Exception as e:
            print(f"[ERROR] > {e}")



print("""
Developer: Leo Power
Dev Website: https://powerthecoder.xyz/
GitHub: https://github.com/powerthecoder
""")
print()
print("""
1) Deposit
2) Withdraw
3) Balance

type '0' to get this menu again
""")
print()
x = 0 
while (x != 1):
    Main()
