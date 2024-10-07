#
import random
import string

lower = string.ascii_lowercase
uppper = string.ascii_uppercase
print(uppper)
print(string.ascii_letters)
symbols = "!@#$%^&*()-+[]{}"
numbers = "0123456789"
all = lower + uppper + symbols + numbers

while True:
    print("choose an option :\n\t1) create a password\n\t2) exit")
    choise = input("your choice : ")
    if choise == "1":
        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(password)
    elif choise == "2":
        break
    else:
        print("invalid option")
