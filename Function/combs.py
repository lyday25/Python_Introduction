combs = []
def combs1():
    
    for x in [1,2,3]:
        
        for y in [3,1,4]:
            
            if x != y:
                
                combs.append((x, y))
           
    print(combs)
    
# I am calling the function declared above
       
combs1()