# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
x=0
threshold=13
basket=[]
for i in list1:
    #print(i)
    x=x+i
    #print(x)
    if x>=threshold:
        #print(x)
        basket.append(x)
        print(basket)
        
#print all the list less than 39
print("All the list less or equal to 29")
y=0        
hold=29
collate=[]        
for p in list1:
    
    y=y+p
    if y<=hold:
        #print(y)
        collate.append(y)
        print(collate)  
        
print("Another task on list")
#task 4 - a python code to determine duplicate
duplicatebasket=[]
emptybasket=[]
listoffruits=["banana" , "watermelon" , "carrot" , "orange" , "pawpaw" , "orange", "banana"]
for f in listoffruits:
    #print(f)
    emptybasket.append(f)
    if emptybasket.count(f)>1:
        duplicatebasket.append(f)
        print(duplicatebasket)
    
#task 5 - summation of list of numbers
total=0
listofnumbers=[400, 200, 50, 10, 19, 150, 0, 5]
for i in listofnumbers:
    total=total+i
print(total)
#task 6 - multiplication of the above numbers
multiply=1
listofnumbers2=[40, 20, 5, 10, 9, 15]
for i in listofnumbers2:
    multiply=multiply*i
print(multiply)
#division of the above result
result=multiply/1000
print(result)
if result>100:
    print("Hurray the result is greater than 100")
    output=(result/10)+5
    print(output)
else:
    output1=result+500
    print(output1)
    
#task 7 - 

    


      
    