from datetime import datetime
import webbrowser

helloIntent = ["hi","hello","hey","hi there","good morning","good evening",]
byeIntent = ["bye","good bye","tata","see you","take care"]

helloReply = "Hello User !!!"
byeReply = "Bye, Take Care !!!"

date = datetime.now().date()

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print(helloReply)
    elif msg in byeIntent:
        print(byeReply)
    elif msg == "date please":
        print(date)
    elif msg == "time please":
        time = datetime.now().time()
        print(time)
    elif msg.startswith("open"):
        t = msg.split()
        webbrowser.open(t[1]+".com")
    else:
        print("I don't understand...")

