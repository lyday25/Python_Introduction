def purchase():
    print("What did you buy")
    bread=input()
    print("enter the amount")
    breadamount=float(input())
    print("What else did you buy")
    fish=input()
    print("enter the amount")
    fishamount=float(input())
    total=breadamount+fishamount
    print("My purchases are " + bread + "," + str(breadamount) + "," + fish + "," + str(fishamount) + "," + str(total))   
    
purchase()   

