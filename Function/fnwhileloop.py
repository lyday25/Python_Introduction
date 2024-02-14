
def findpasscode(passcode):
    
    password=""
    while passcode != password:
        
        print('What is the password?')
        
        password = input()
        
    print('Yes, the password is ' + password + '. You may enter.')
    
# I am calling the function declared above
findpasscode("food")