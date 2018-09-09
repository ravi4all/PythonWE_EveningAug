def atm():
    totalBal = 10000
    pin = input("Enter PIN: ")

    amount = int(input("Enter the amount : "))
    if amount > totalBal:
        # print("Insufficient Balance")
        raise ValueError("Insufficient Balance")

    totalBal -= amount
    print("Remaining bal is",totalBal)
    input("You want slip Y/N ? ")

try:
    atm()
except ValueError as err:
    print(err)