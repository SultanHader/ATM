import time

print("ENTER YOUR Deposit card Here")
time.sleep(1)

password = 1212
balance = 100

pin = int(input("Enter your pin: "))
while True:
    if pin == password:
        print("""
        1: DEPOSIT
        2: WITHDRAW 
        3: CHECK BALANCE 
        4: EXIT 
        """)
        try:
            option = int(input("ENTER YOUR CHOICE: "))
        except ValueError:
            print("Enter a VALID OPTION")
            continue

        if option == 3:
            print("Your current balance is", balance)
        elif option == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > balance:
                print("INSUFFICIENT BALANCE")
            else:
                balance -= amount
                print(amount, "is debited from your account")
                print("Your current updated balance is", balance)
        elif option == 1:
            amount = int(input("Enter the amount you want to deposit: "))
            balance += amount
            print(amount, "is deposited to your account")
            print("Your current updated balance is", balance)
        elif option == 4:
            print("Thank you for using our service!")
            break
        else:
            print("Enter a VALID OPTION")
    else:
        print("YOU ENTERED the WRONG PIN")
        pin = int(input("Enter your pin: "))

