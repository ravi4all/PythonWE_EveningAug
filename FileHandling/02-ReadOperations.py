# by default mode is 'r'
file = open('data.txt')

# data = file.read(15)

# data = file.readlines()

# data = file.readline()

file.seek(15)
data = file.read()
print(data)

file.close()