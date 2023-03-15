import random
import sys
import datetime


 
class ATM():
    def __init__(self, name, account_pin, balance = 500):
        self.name = name
        self.account_pin = account_pin
        self.balance = balance
        
    
        # datetime_object = datetime.datetime.now()
        # print(datetime_object)

        
    def account_detail(self):
        print("\n ---  ACCOUNT DETAIL ---  ")
        print( f"Account Holder: {self.name.upper()}")
        # print(f"Account pin: {self.account_pin}")
        print(f"Available balance: {self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: ", self.balance)
       
        
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} only.")
            print("Try with lesser amount than balance.")
            datetime_object = datetime.datetime.now()
            print(datetime_object)
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} withdrawal successful!")
            print("Current account balance: ", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: ", self.balance)
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        print()
 
    def transaction(self):
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        
        print()

        print("""
            *** TRANSACTION ***
        
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit:"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw:"))
                    atm.withdraw(amount)
                elif option == 5:
                      
                    print(f"""
                    
                printing receipt..............
          
              Transaction is now complete....
              
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()} 
              Available balance: {self.balance}  
               Thanks......                 
          
              """)

            # a = open('B.txt','w')
            # new = a.write(
            # Transaction number: {random.randint(10000, 1000000)} 
            # Account holder: {self.name.upper()} 
            # Available balance: {self.balance}  
            # )
    
                 
 
print(" *** WELCOME TO ATM SYSTEM ***")
print("  ")
print("     --- INSERT YOUR CARD ---")

print("      --- INSERT CARD SUCCESFULLY ---")

name = input("Enter your name: ")
account_pin = input("Enter your pin: ")
print("  Account in progress successfully......\n")
 
atm = ATM(name,account_pin)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    
       Thanks..... 
       Visit us again !                     
    
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
    
