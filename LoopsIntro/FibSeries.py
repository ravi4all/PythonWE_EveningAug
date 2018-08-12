# swapping of two numbers
# a,b = 10,12
# a,b = b,a

# Fibonacci Series - 0 1 1 2 3 5 8 13 21 34....

a = 1
b = 0

while b < 100:
    print(b, end=' ')
    a,b = b,a+b
