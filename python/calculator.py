operator=input("enter an operator (+,-,*,/,%):")
num1=float(input("Enter the value of num1:"))
num2=float(input("Enter the value of num2:"))

if operator=="+":
    print (num1+num2)
elif operator=="-":
    print (num1-num2)
elif operator == "*":
    print(num1*num2)  
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1%num2)
else:
    print(f"the {operator} is not valid")       