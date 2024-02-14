#python code to add numbers together
list1=[2,56,78,34,23,21]
total=0
for y in list1:
    total=total+y
print(total)
#check if total is greater than 50, if yes, divide by 20 and add 19. otherwise add 500
if total>50:
    print("Hurray total is greater than 50")
    result=(total/20)+19
    print(result)
else:
    result=total+500