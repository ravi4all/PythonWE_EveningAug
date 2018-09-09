# def temp_conv(c):
#     return 9/5 * c + 32

temp = [32.3,35.6,38.7,31.5,34.6]

# f = temp_conv(temp)
# print(f)

# for t in temp:
#     f = temp_conv(t)
#     print(f)

# f = list(map(temp_conv, temp))
# print(f)

f = list(map(lambda c : 9/5 * c + 32, temp))
print(f)

# def even(num):
#     return num % 2 == 0

numbers = [i for i in range(1,51)]

# n = list(filter(even, numbers))
# print(n)

n = list(filter(lambda n : n % 2 == 0, numbers))
print(n)