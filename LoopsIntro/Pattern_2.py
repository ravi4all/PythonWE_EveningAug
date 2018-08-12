##for i in reversed(range(1,6)):
##    print('*'*i)

for i in reversed(range(1,6)):
    for j in reversed(range(1,i+1)):
        print(j,end='')
    print()
