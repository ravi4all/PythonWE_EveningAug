helloIntent = ["hi","hello","hey","hi there","good morning","good evening",]
byeIntent = ["bye","good bye","tata","see you","take care"]

helloReply = "Hello User !!!"
byeReply = "Bye, Take Care !!!"

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print(helloReply)
    elif msg in byeIntent:
        print(byeReply)
    else:
        print("I don't understand...")

