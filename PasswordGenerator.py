import random
import string
Length = int(input("Enter length of password: "))

Chars = string.ascii_letters
Chars += string.digits
Chars += string.punctuation

Password = ''.join([random.choice(Chars) for i in range (Length)])

print("Your random password is:", Password)