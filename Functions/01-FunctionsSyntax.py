# Local Scope
# Global Scope

a = 10
b = 5

def add():
    # local variables
    a = 15
    b = 12
    c = a + b
    print("Sum is",c)

def sub():
    c = a - b
    print("Diff is",c)

add()
sub()