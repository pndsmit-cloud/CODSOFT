import random 
import string
# take password length frpom user 

length = int(input("Enter the length of the password: "))

#character to be used in password 
characters = string.ascii_letters + string.digits + string.punctuation

#generate password 
password = " "
for i in range(length):
    password += random.choice(characters)

#display the generated password
print("\nGenerated password: ", password)
