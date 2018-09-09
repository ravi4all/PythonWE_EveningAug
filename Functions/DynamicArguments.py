# *args, **kwargs

# def emp(name,age,*address):
#     print(name,age,address)
#
# emp('Ram',30,'Delhi','Pune')

def emp(**details):
    print(details)

emp(name='Ram',age=30,company='TCS')
emp(name='Shyam',age=29)
emp(name='Aman',company='HCL',address='Delhi')