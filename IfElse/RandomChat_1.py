helloIntent = ["hi","hello","hey","hi there","good morning","good evening",]
byeIntent = ["bye","good bye","tata","see you","take care"]

helloReply = "Hello User !!!"
byeReply = "Bye, Take Care !!!"

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    for i in range(len(helloIntent)):
        if msg == helloIntent[i]:
            print(helloReply)

    for i in range(len(byeIntent)):
        if msg == byeIntent[i]:
            print(byeReply)

