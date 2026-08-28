from colorama import Fore
import secrets
import pyperclip
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id


print(Fore.MAGENTA + r"""__________                          ________
\______   \_____    ______ ______  /  _____/  ____   ____
 |     ___/\__  \  /  ___//  ___/ /   \  ____/ __ \ /    \
 |    |     / __ \_\___ \ \___ \  \    \_\  \  ___/|   |  \
 |____|    (____  /____  >____  >  \______  /\___  >___|  /
                \/     \/     \/          \/     \/     \/""")

print(Fore.MAGENTA + r"""______         _____                                    
| ___ \       |  __ \                                   
| |_/ /_   _  | |  \/ ___ _ __ ___  _ __ ___   ___ _ __ 
| ___ \ | | | | | __ / _ \ '_ ` _ \| '_ ` _ \ / _ \ '__|
| |_/ / |_| | | |_\ \  __/ | | | | | | | | | |  __/ |   
\____/ \__, |  \____/\___|_| |_| |_|_| |_| |_|\___|_|   
        __/ |                                           
       |___/                                            """)

print(Fore.RESET)

# Verifying if the salt (the file that will be combined with the master password to create the key) exist if not, creating it.
if os.path.exists("salt.txt"):
    with open("salt.txt", "rb") as f:
        salt = f.read()
else:
    salt = os.urandom(16)
    with open("salt.txt", "wb") as f:
        f.write(salt)


# Defining the setting of hashing
kdf = Argon2id(
    salt=salt,
    length=32,
    iterations=3,
    lanes=4,
    memory_cost=128 * 1024
)


print("What's your master password (a password that you need to remember that will be used to crypt your password)")
masterPassword = input()


# Creating the key to crypt/decrypt
key = base64.urlsafe_b64encode(kdf.derive(masterPassword.encode()))
f = Fernet(key)


while True: 
    print("Do you want to see your password (1), to create password (2) or to leave (3)?")
    mode = input()

    # Verifying if the input is valid
    isNumber = True
    try:
        int(mode)
    except:
        isNumber = False

    if isNumber == False or int(mode) < 1 or int(mode) > 3:
        print(Fore.RED + "Must be a number between 1 and 3.")
        print(Fore.RESET)
    else:     


        # Verify if passwords.enc exists. If yes, decrypt and show the password.
        if int(mode) == 1:
            if os.path.exists("passwords.enc") == False:
                print(Fore.RED + "You don't have password.")
                print(Fore.RESET)
            else:
                with open("passwords.enc", "rb") as passFile:
                    for line in passFile:
                        print(f.decrypt(line))

        # Generate a password as the user wants then crypt it and write it in passwords.enc + the service that it s used for
        elif int(mode) == 2:
            while True :
                print("How many characters do you want ?")
                numCharacters = input()

                # Verifying if the input is valid
                isNumber = True
                try:
                    int(numCharacters)
                except:
                    isNumber = False

                if isNumber == False or int(numCharacters) <= 0:
                    print(Fore.RED + "Must be a number higher than 0.")
                    print(Fore.RESET)
                else:
                    break

            # Defining what kind of password the user wants
            while True:
                print("Do you want only number (1), only letter (2), both (3), number and special characters (4), letter and special characters (5), all (6) ?")
                choice = input()

                # Verifying if the input is valid
                isNumber = True
                try:
                    int(choice)
                except:
                    isNumber = False

                if isNumber == False or int(choice) < 1 or int(choice )> 6: # Is the input a number between 1 and 6
                    print(Fore.RED + "Must be a number between 1 and 6.")
                    print(Fore.RESET)
                else:
                    break


            # All the possible characters
            options = {
                1: "0123456789",
                2: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                3: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                4: "0123456789!@#$%^&*()-+?.,;",
                5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
                6: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
            }
            characters = options.get(int(choice))


            # Creating the password by mixing x times a random letter choosed in the list of characters
            password = ''.join(secrets.choice(characters) for _ in range(int(numCharacters)))


            # To remember which password is for what
            print("For which service is this password ?(website, email...)")
            service = input()


            # Easier to write the hash of one variable
            serviceAndPass = service + ": " + password


            # Show the password at the screen
            print(Fore.GREEN + "Your password is: " + password + "\nIt has been saved in passwords.enc.")
            print(Fore.RESET)


            # Hash the password and write the result
            with open("passwords.enc", "ab") as passFile:
                passFile.write(f.encrypt(serviceAndPass.encode()) + b"\n")


            # Allow the user to copy the password
            print(Fore.YELLOW + "Do you want to copy it to the clipboard ? (y/n)")
            clipboard = input().lower()

            if clipboard == "y":
                pyperclip.copy(password)
                print(Fore.GREEN + "Password copied to clipboard.")
                print(Fore.RESET)
            else:
                print(Fore.WHITE + "Password not copied to clipboard.")
                print(Fore.RESET)

        # To leave the loop
        elif int(mode) == 3:
            print("Goodbye.")
            break