###-------###
###Imports###
###-------###
from colorama import Fore
import secrets
import pyperclip
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id


###---------###
###Fonctions###
###---------###
def greetings(): # The name of the project and me (the author)
    print(Fore.MAGENTA + r"""______               _____            
| ___ \             |  __ \           
| |_/ /_ _ ___ ___  | |  \/ ___ _ __  
|  __/ _` / __/ __| | | __ / _ \ '_ \ 
| | | (_| \__ \__ \ | |_\ \  __/ | | |
\_|  \__,_|___/___/  \____/\___|_| |_|
                                      
                                      """)

    print(Fore.MAGENTA + r"""______         _____                                    
| ___ \       |  __ \                                   
| |_/ /_   _  | |  \/ ___ _ __ ___  _ __ ___   ___ _ __ 
| ___ \ | | | | | __ / _ \ '_ ` _ \| '_ ` _ \ / _ \ '__|
| |_/ / |_| | | |_\ \  __/ | | | | | | | | | |  __/ |   
\____/ \__, |  \____/\___|_| |_| |_|_| |_| |_|\___|_|   
        __/ |                                           
       |___/                                            """)

    print(Fore.RESET)


def verify_input(value): # To verify if the input is a int
    try:
        int(value)
        return True
    except ValueError:
        return False


def error(text): # To look cleaner
    print(Fore.RED + text)
    print(Fore.RESET)


def success(text): # To look cleaner
    print(Fore.GREEN + text)
    print(Fore.RESET)



def information(text): # To look cleaner
    print(Fore.YELLOW + text)
    print(Fore.RESET)


###--------------------###
###Variable/Dictionnary###
###--------------------###
options = { # All the possible characters
    1: "0123456789",
    2: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    3: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    4: "0123456789!@#$%^&*()-+?.,;",
    5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
    6: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
}


###---------###
###Main code###
###---------###
greetings()

print("What's your master password (a password that you need to remember that will be used to crypt your password)")
masterPassword = input()

# Verifying if the salt (the file that will be combined with the master password to create the key) exist if not, creating it.
if os.path.exists("salt.txt"):
    with open("salt.txt", "rb") as f:
        salt = f.read()
else:
    salt = os.urandom(16)
    with open("salt.txt", "wb") as f:
        f.write(salt)

# Defining the setting of crypting
kdf = Argon2id(
    salt=salt,
    length=32,
    iterations=3,
    lanes=4,
    memory_cost=128 * 1024
)

# Creating the key to crypt/decrypt
key = base64.urlsafe_b64encode(kdf.derive(masterPassword.encode()))
f = Fernet(key)

while True: # Main loop
    print("Do you want to see your password (1), to create password (2) or to leave (3)?")
    mode = input()

    if verify_input(mode) == False or int(mode) < 1 or int(mode) > 3:
        error("Must be a number between 1 and 3.")

    else:
        if int(mode) == 1:
            if os.path.exists("passwords.enc") == False: # Does the file exist
                error("You don't have password.")

            else:
                with open("passwords.enc", "rb") as passFile:
                    for line in passFile: # Read line by line
                        try:
                            print(f.decrypt(line))
                        except:
                            error("Wrong master password.")

        elif int(mode) == 2:
            while True:
                print("How many characters do you want ?")
                numCharacters = input()

                if verify_input(numCharacters) == False or int(numCharacters) <= 0:
                    error("Must be a number higher than 0.")

                else:
                    break

            while True:
                print("Do you want only number (1), only letter (2), both (3), number and special characters (4), letter and special characters (5), all (6) ?")
                choice = input()

                if verify_input(choice) == False or int(choice) < 1 or int(choice )> 6:
                    error("Must be a number between 1 and 6.")
                    
                else:
                    break

            characters = options.get(int(choice)) # Set what characters

            password = ''.join(secrets.choice(characters) for _ in range(int(numCharacters))) # Create the password

            print("For which service is this password ?(website, email...)")
            service = input()
            serviceAndPass = service + ": " + password

            success("Your password is: " + password + "\nIt has been saved in passwords.enc.")

            with open("passwords.enc", "ab") as passFile: # To write the crypted password
                passFile.write(f.encrypt((serviceAndPass).encode()) + b"\n")

            information("Do you want to copy it to the clipboard ? (y/n)")
            clipboard = input().lower()

            if clipboard == "y":
                pyperclip.copy(password)
                success("Password copied to clipboard.")
            else:
                information("Password not copied to clipboard")

        elif int(mode) == 3:
            print("Goodbye.")
            break