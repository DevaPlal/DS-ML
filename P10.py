import re

def is_valid_password(password):
 
    if len(password) < 8:
        return False

    
    if not re.search(r'[a-z]', password):
        return False

   
    if not re.search(r'[A-Z]', password):
        return False

    
    if not re.search(r'[0-9]', password):
        return False

    
    if not re.search(r'[$#@]', password):
        return False

   
    return True


password = input("Enter a password: ")


if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")
