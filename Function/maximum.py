
maximum=[20,60,70,90,500,700,800,99]
       
def findmax(a):
      for item in maximum:
        if item > a:
            return print(item)
        else:
            print("No maximum items")    
    
print("This is the maximum number above the threshold " + str(findmax(330)))