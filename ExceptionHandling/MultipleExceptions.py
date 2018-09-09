def calc():
    try:
        x = int(input("Enter first number : "))
        y = int(input("Enter second number : "))

        a = x + y
        print("Sum is",a)

        b = x - y
        print("Sub is",b)

        c = x / y
        print("Div is",c)

        d = x * y
        print("Mul is",d)

    except ValueError:
        print("Invalid Input, Only digits are allowed")
        calc()

    except ZeroDivisionError:
        print("Cannot divide by zero")
        calc()

calc()