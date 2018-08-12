# break - break the loop
# for i in range(100):
#     print(i)
#     if i == 10:
#         break

# continue - will skip the current iteration
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

numbers = [2,4,6,8,4,4,6,0,7,4,12]
for num in numbers:
    if num == 0:
        continue
    a = 2 % num
    print(a)