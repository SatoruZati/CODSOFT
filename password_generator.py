import random

def password(n):
    passwordstr = "" 
    passwordstr = passwordstr + chr(random.randint(65,90))
    charlist = [chr(random.randint(97,122)),chr(random.randint(65,90)),chr(random.randint(33,64))]

    for i in range(n-1):
        passwordstr = passwordstr + random.choice(charlist)

    return passwordstr

password_length = int(input("Enter length of your password: "))
print("Password is: " + password(password_length))