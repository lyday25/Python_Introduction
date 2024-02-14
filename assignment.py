#task to add yam to a list of item given
listofitems=["banana" , "groundnut" , "apple" , "pawpaw" , "orange"]
listofitems.append("yam")
print(listofitems)

#check if groundnut is in the list
for i in listofitems:
    if i=="groundnut":
        print("True groundnut is in the list of items")
        
#a python code that loops through the list and print them out
for food in listofitems:
    print(food)
    
#python code that removes groundnut
listofitems.remove("groundnut")
print(listofitems)
 

    



