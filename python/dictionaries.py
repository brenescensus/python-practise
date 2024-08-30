#dictionarie is a variable that stores a collection of data in key and value pairs
#dictionaries are ordered,changeable and does not allow duplicates
#dictionaries are written with curly brackets

menu={"burger":300,"pizza":1000,"fries":200}
print("***************MENU***********************")
for key,value in menu.items():
    
    print(f"{key}  {value:0}")
    print()

cart=[]
total=0
while True:
    order=input("what would you like to order?").lower()
    if order in menu:
        quantity=int(input("how many would you like to order?"))
        total=total+(quantity*menu[order])
        cart.append((order,quantity,total))
        print(f"{quantity} {order} has been added to your cart")
    elif order=="q":
        break    
    else:
        print("sorry we dont have that item")


print(f"the total is {total}")        
        
        
   
