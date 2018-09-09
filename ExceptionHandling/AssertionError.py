def atm():
    totalBal = 10000
    pin = input("Enter PIN: ")

    amount = int(input("Enter the amount : "))

    assert (amount < totalBal), "Insufficient Balance"

    totalBal -= amount
    print("Remaining bal is", totalBal)
    input("You want slip Y/N ? ")


try:
    atm()
except AssertionError as err:
    print(err)