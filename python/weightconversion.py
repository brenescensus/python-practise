#the conditional operators are used to perform an operation if a certain condition is satisfied
#conditional expressions is a short form afor an if else atatement

age =2

weight=float(input("enter your weight in pounds or kg:"))
unit=input("enter the unit of weight (K / L):")

if unit =="K":
    weight=weight*2.205
    Unit="Kgs"
    print(f"your weight is {round(weight,2)} {Unit}")
elif unit== "L":
    weight=weight/2.205
    Unit="Libs"
    print(f"your weight is {round(weight,2)} {Unit}")
else:
    print(f"the {unit} is not valid");    
    
    
    #conditional expression
    
age="age is invalid" if age==2 else "age is valid"
print(age)