def calc(x,y):

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub

# x = calc(10,12)()
# print(x)

x = calc(10,12)
a = x[0]()
b = x[1]()
print(a,b)