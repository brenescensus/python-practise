# a string is a collection of characters
name=str(input("Enter your correct name:"))



#the string has several methods that can be used to manipulate the string
len(name)
# result=len(name)#prints the length of the stringresult=
# result=name.upper()#prints the string in uppercase
# result.lower()#prints the strings in lower case
# result=name.find("e") #returns the first occurence of the character
# result=name.isalpha() #chhecks if the string is alphabetic returns false a string contains whitespaces and numbers
result=name.isdigit() #chaecks if the string is numeric returns false a string contains whitespaces and alphabets
print(result)

result=name.__contains__("e") #checks if the string contains a character
print(result)   



# print(help(str))



#string indexing
#string=[start:stop:step]
result=name[0:5]#prints the first 5 charactesa
result=name[0:15:3]#prints the first 5 charactes and skips 2 steps
print(result)  


#email slicer exercise
#create a program that takes an email address from the user and prints the username and domain name
email=input("enter your email address:")
symbol=email.index("@")
username=email[:symbol]
domain=email[symbol+1:] 
print(f"your username is {username} and your domain is {domain}")
 


