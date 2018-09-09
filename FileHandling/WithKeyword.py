# file = open('data.txt', 'r')
# file.read()
# file.close()

with open('data.txt','r') as file:
    file.read()

print("File Closed...")