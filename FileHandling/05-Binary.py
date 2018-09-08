file = open('ball_2.png', 'rb')
data  = file.read()
# print(data)
file.close()

file = open('ball_3.png','wb')
file.write(data)
file.close()