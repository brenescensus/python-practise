x=2
x=x+1 #is the sama thing as x+=1
x*2 #is the same thing as x*=2
x/2 #is the same thing as x/=2
x=x-1 #is the same thing as x-=1
x=x%2 #is the same thing as x%=2
x=x**2 #is the same thing as x**=2
x=x//2 #is the same thing as x//=2

y=22
print(pow(y,2))

print(abs(y))
 #absolute value of a number is the distance of a number from 0 on the number line
 
 #PYHRON HAS SEVERAL MATH FUNCTIONS THAT CAN BE USED TO PERFORM MATH OPERATIONS
import math
import random
x=2
print(round(math.sqrt(x),2))
print(math.ceil(2.3))
print(math.floor(2.3))
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.pow(2,3))
print(math.log(2,3))
x=random
# calculating the area of a circle
radius=float(input("enter the radius of the circle:"))
#area=pi*r^2
print(f"the area is {round(math.pi*radius**2,2)}")  

 
 #calculating the hypotenuse of a triangle
 #a^2+b^2=c^
length=float(input("enter the lenght of the triangle:"))
width=float(input("enter the width of the triangle:"))
hypotenuse=math.sqrt(pow(length,2)+pow(width,2))
print(f"the hypotenuse is {round(hypotenuse,2)}")  