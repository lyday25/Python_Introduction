animal=["Yes",  "Yes", "Yes", "No","Yes",
        "Yes", "Yes","Yes","Yes", "No",
        "Yes", "No", "Yes", "No",   "No",
        "Yes","Yes", "Yes", "Yes", "Yes",
        "No",  "No",  "Yes","Yes", "No",
        "Yes"]
 
 # count the number of cows present in the list above. Indicate Yes if present.
cowcount=0
cowspresent=[]
def count_cows():
    
    for i in animal:
        if i =="Yes": #meaning present
            cowcount=cowcount=+1
            cowspresent.append(i)
            
        else:
            continue
    print(cowspresent.count(i))
    
# call the function for the final outcome
count_cows()
