# the logical operators are used to perform an operation if a certain condition is satisfied
#python logical operators include and,or,>,<,>=,<=,!=,==



age =int(input("enter your age"))
# if age !=10:
#     print("you are not 10 years old")
# if age>18:
#     print ("you can now aquire an id card")
# elif age==16 or age==30:
#     print("this is a special age ")   
# elif age>0 and age<18:
#     print ("you are too to young to acqitre an id card")    
# elif age>100:
#     print ("you are too old to acqitre an id card")
# elif age==16 or age==30:
#     print("this is a special age ") 
# else:
#     print("the value entered  is not valid")  
    
# print("The end of the program")        



#use of a conditional expression
#this is the shortestway to write an if else statement,it is the same as a tenary operator
age="you are an adult" if age>18 else "you are still young"
print(age)