# AND, OR, NOT

while True:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hey" or msg == "hi":
        print("Hi There...")
    elif msg == "bye" or msg == "bie" or msg == "see you":
        print("Bye")
    elif msg == "python" or msg == "java" or msg == "php":
        print("Programming language")
    else:
        print("I don't understand")