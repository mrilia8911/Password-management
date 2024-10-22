import random
import string

# Define character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "!@#$%^&*()-+[]{}"
numbers = "0123456789"
all = lower + upper + symbols + numbers

# Print character sets for reference
print(upper)
print(string.ascii_letters)

while True:
    print("Choose an option: \n\t1) Create a password\n\t2) Exit")
    choice = input("Your choice: ")
    
    if choice == "1":
        social_media = input("For which social media do you want this password? : 1.instagram/facebook | 2.tonkeeper | 3.email | 4.X | 5.other :")
        
        if social_media == "1":
            password = "".join(random.sample(all, 6))
            print(f"Generated password: {password}")
        elif social_media == "2":
            password = "".join(random.sample(numbers, 4))
            print(f"Generated password: {password}")
        elif social_media == "3":
            password = "".join(random.sample(all, 15))
            print(f"Generated password: {password}")
        elif social_media == "4":
            password = "".join(random.sample(all, 10))
            print(f"Generated password: {password}")
        elif social_media == "5":
            password = "".join(random.sample(all, 12))
            print(f"Generated password: {password}")
        else:
            print("Invalid option for social media choice.")
        
        # Save the password to a file
        try:
            with open("passwords.txt", "a") as file:
                file.write(f"{social_media}: {password}\n")
            
            # Read and print the contents of the file
            with open("passwords.txt", "r") as file:
                print("\nSaved Passwords:")
                print(file.read())
        except Exception:
            print(f"An error occurred: {e}")
    
    elif choice == "2":
        break
    else:
        print("Invalid option")
