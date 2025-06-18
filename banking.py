class bank:
       
    def deposit(self, amount, intialbal):
        if(amount < 0):
            print("\nDeposit amount cannot be negative")
            return 0
        else:
            return amount
    def withdraw(self, amount, intialbal):
        if(amount < 0):
            print("\nWithdraw amount cannot be negative")
            return 0
        elif(amount > intialbal):
            print("\nInsufficient balance")
            return 0
        else:
            return amount
    def display_balance(self, balance):
        print("\nYour current balance is: Rs.", balance)

obj = bank()
print("\n*****************************")
print("Welcome to the Banking System")
print("*****************************")
balance= int(input("Enter the initial balance: Rs."))

isrunning = True
while isrunning:
    choice = int(input("\nEnter\n 1 to Show balace\n 2 for Deposit\n 3 for Withdraw\n 4 to Exit\n") )
    match choice:
        case 1:
            obj.display_balance(balance)
        case 2:
            deposit_amount = int(input("\nEnter the amount to deposit: "))
            balance += obj.deposit(deposit_amount, balance)
            
        case 3:
            withdraw_amount = int(input("\nEnter the amount to withdraw: "))
            balance -= obj.withdraw(withdraw_amount, balance)
        
        case 4:
            print("\nThank you for using the Banking System")
            print("******************************\n")
            isrunning = False
            break
        case _:
            print("\nInvalid choice, please try again")

