try:
    file = open('data.txt','w')
    data = ["hello","world"]
    file.write(data[0])
except BaseException as ex:
    print(ex)
else:
    print("I will execute if except will not execute")
finally:
    print("I will always execute...")
    file.close()
