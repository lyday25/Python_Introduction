
def namevowel():
    # Set up name variable with input
    name = str(input('Enter your name: '))
    # Check whether name has a vowel
    if set('aeiou').intersection(name.lower()):
        print('Your name contains vowel.')
    else:
        print('Your name does not contain a vowel.')
 
    # Iterate over name
    for letter in name:
        print(letter)
 
# Call the function
namevowel()