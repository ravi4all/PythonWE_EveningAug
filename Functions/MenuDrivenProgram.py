def add(x,y):
    z = x + y
    print(z)

def sub(x,y):
    z = x - y
    print(z)

print("""
1. Add
2. Sub
""")

userChoice = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

# if userChoice == "1":
#     add(num_1, num_2)
# elif userChoice == "2":
#     sub(num_1,num_2)

operations = {
    "1" : add,
    "2" : sub
}

operations.get(userChoice)(num_1, num_2)