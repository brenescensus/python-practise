#while loop is used to perform a certain operation while a given condition is true

age=int(input("entre yiur age"))

while age<0:
    print("you have entered an invalid value")
    age=int(input("entre yiur age"))
print(f"hello {age}")   


principle=int(input("enter the pricniple amount"))

while principle<=0:
    print("the principle cannot be zero")
    principle=int(input("enter the pricniple amount"))
 
rate=int(input("enter the given rate")) 
while rate<=0:
    print("the rate cannot be zero or less")
    rate=int(input("enter the given rate")) 
time=int(input("enter the given time"))
while time<=0:
    print("the rate cannot be zero or less")

    time=int(input("enter the given time"))


total=principle * pow((1+rate/100),time)
print(round(total,2))
    
    