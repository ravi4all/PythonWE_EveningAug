def add(x,y):
    z = x + y
    print("sum is",z)

def sub(x,y):
    z = x - y
    print("diff is",z)

def mul(x,y):
    z = x * y
    print("mul is",z)

def div(x,y):
    z = x / y
    print("div is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

userChoice = input("Enter your choice : ")

fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}

operations.get(userChoice)(fnum,snum)