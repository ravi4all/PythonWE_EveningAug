def calc(x,y,opr):
    z = x + opr + y
    # z = '12' + '+' '15'
    # z = '12 + 15'
    # evaluate
    result = eval(z)
    print("Result is",result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

userChoice = input("Enter your choice : ")

fnum = input("Enter first number : ")
snum = input("Enter second number : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}

# operations.get(userChoice)(fnum,snum)
opr = operations.get(userChoice)
calc(fnum,snum,opr)