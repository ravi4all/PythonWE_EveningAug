firstname = input("Enter first name : ")
lastname = input("Enter last name : ")

# msg = "Hello" + " " + firstname.lower() + " " + lastname.lower()

# msg = "Hello" + " " + firstname.swapcase() + " " + lastname.swapcase()

# msg = "Hello" + " " + firstname.upper() + " " + lastname.upper()
#print(msg)

print("Hello {} {}".format(firstname.upper(), lastname.upper()))
