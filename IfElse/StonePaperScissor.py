import random

choices = ["stone","paper","scissor"]

while True:
    user = input("Enter your choice : ")

    cpu = random.choice(choices)
    print("CPU :",cpu)
    if user == cpu:
        print("Match Tie...")
    elif user == "stone" and cpu == "paper":
        print("CPU Win")
    elif user == "paper" and cpu == "scissor":
        print("CPU Win")
    elif user == "scissor" and cpu == "stone":
        print("CPU Win")
    elif user == "stone" and cpu == "scissor":
        print("You Win")
    elif user == "paper" and cpu == "stone":
        print("You Win")
    elif user == "scissor" and cpu == "paper":
        print("You Win")