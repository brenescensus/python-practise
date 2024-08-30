# a collection is a variable that can store multiple values
# python has 3 built in collection types
# list,tuple,dictionary

#list[]
# a list is a collection which is ordered and changeable.allows duplicate members

#tuple()
# a tuple is a collection which is ordered and unchangeable.allows duplicate members

#Set{}
# a set is a collection which is unordered and unindexed.no duplicate members


fruits=["apple","banana","cherry","orange","mango"]


#list methods
#append() adds item to the end of the list
# fruits.append("pineapple")
#pop() removes the last element if the index is not specified
# fruits.pop()
#remove() removes the specified element
# fruits.remove("banana")
#clear() removes all the elements in the list
# fruits.clear()
#insert() inserts an element at the specified position and moves the rest of the elements to the right
fruits.insert(1,"grapes")
#sort() sorts the list in alphabetic order
fruits.sort()
#reverse() reverses the order of the list
fruits.reverse()
# print(fruits)

vegetabale=["carrot","cabbage","tomato"]
cereals=["maize","beans","peas"] 
      
            
# groceries=[fruits,vegetabale,cereals]

        # print()
# print(groceries,end="")


#a quiz game
Questions=["what is the capital of kenya?","what is the capital of uganda?","what is the capital of tanzania?"]
options=[["Nairobi","Kampala","Dodoma","Kigali"],["Nairobi","Kampala","Dodoma","Kigali"],["Kampala","Dodoma","Kigali"]]
guesses=[]
answers=["Nairobi","Kampala","Dodoma"]
final_score=0 
quiz_index=0

print("************************ANSWER THE FOLLOWING QUESTIONS**********************")
for question in Questions:
    print(question)
    for option in options:
        print(option)
        choice=input("Enter your answer:").capitalize()
        if choice==answers[quiz_index]:
            print("CORRECT ANSWER")
            final_score=final_score+1
            guesses.append(choice)
            break
        else:
            print("WRONG ANSWER")
            print(f"the correct answer is {answers[quiz_index]}")
            guesses.append(choice)
            break
    quiz_index+=1    
print(guesses) 
print(final_score)           
total=(final_score/len(Questions)*100) 
print(f"the final score is {total:.2f} %") 
print("*************HURRAY END OF GAME*******************")    
        
     
    
