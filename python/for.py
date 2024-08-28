#for loop is used to give results within a certain range

for x in range(2):
    print(x)
    
#printing prime numbers
# num=13
# for i in range(2,num):
#     if num%i==0:
#         print("is prime")
#     else:
#         print("prime")  
        
# print("hurray") 
# isprime=True
# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return not isprime
#             # print(f"{num} is not prime number")
            
#         else:
#             return isprime
#             # print(f"{num} is a prime number")
      
     
# isprime(13)

#nested loops

rows=int(input("enter the number of rows"))
colums=int(input("enter the number of columns"))
symbol=input("enter a symbol")


for i in range(rows):
    for j in range(colums):
        print(symbol,end=" ")
    print((()))    