print("Hello World")
x="hello there"
y="brenes"
z=4


# def myfunc():
#     print("hello world")


# myfunc()
# def myfunc(x):
#     if x>0:
#         print("number is positive")
#     elif(x<0):
#         print("number is negative")
#     else:
#       print("number is zero")
      
# myfunc(6)
# def SumFunc(a,b):
#     print(a+b)
    
# SumFunc(3,4)  

# Car=["Jeep","Volvo","BMw"]
# Car={"name":"jeep",
#      "model":2019,
#      "year":2024
#      }
Numberlist=[20,34,57,67,45,45,67,32,89,9]
for i in Numberlist:
    if i%2==0:
        print(i)
        
numbers = [20,34,57,67,45,45,67,32,89,9]
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:  # Check if the number is even
        print(numbers[index])
    index += 1        
    
print(Numberlist[:4])