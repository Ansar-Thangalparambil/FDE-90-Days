balance=int(input("Enter your balance : "))
withdraw = int(input("Enter the amount to withdraw : "))


if balance <= 0 :
    print("Insufficient account  balance")
elif withdraw <= 0 :
    print ("Your Transaction rejected")
elif withdraw>balance :
    print("Insufficient account balance")
else : 
    remaining_balance = balance-withdraw
    print("Withdrawal successfull")
    print("Remaining balance is :",remaining_balance)
