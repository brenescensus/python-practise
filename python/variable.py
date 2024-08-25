#a varaible is a value that is used to store data in a program


x=2 # an integer
y="hello there" # a string
z=2.3 # a float
r=True# a boolean
print(x,y,z,r)

#typecasting
#this involves converting a datataype from one form to another 
#there are two types of typecasting
#implicit and explicit
#implicit is when the datatype of a variable changes automatically eg when an arithmetic operation is perfomed on it

t=4
u=2.3
t=t/u
print(t)
#x=1.7391304347826089 the result has been converted from an integer to a float number automatically

#explicit typecasting is when the variable  datatype is manually convereted to another datatype
#this is done using the built in functions
#int(),float(),str(),bool()

x=1.7391304347826089 
print(type(x))
#<class 'float'> the datatype of x is float
x=int(x)
print(x) # the result is 1 thus the valuse of x has been converted from a float to an integer
print(type(x))

y=True
z="hello world"

t=int(y)
print(t)

y=str(y)
print(y)

#when converting to boolean any nuber other than 0 is true AND any string other than an empty string is trueCLEAR



y="22"
z="hello"

print(str(y))
# print(  (z))
#converting a string that is not a number to an integer will result in an error
