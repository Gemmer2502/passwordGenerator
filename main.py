from colorama import Fore
import secrets
import pyperclip


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


while True :
    print("How many characters do you want ?")
    num_characters = input()

    isNumber = True
    try:
        int(num_characters)
    except:
        isNumber = False

    if isNumber == False or int(num_characters) <= 0: # Is the input a positive number
        print(Fore.RED + "Must be higher than 0.")
        print(Fore.RESET)
    else:
        break


while True:
    print("Do you want only number (1), only letter (2), both (3), number and special characters (4), letter and special characters (5), all (6) ?")
    choice = input()

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

options = {
    1: "0123456789",
    2: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    3: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    4: "0123456789!@#$%^&*()-+?.,;",
    5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
    6: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
}

characters = options.get(int(choice))

password = ''.join(secrets.choice(characters) for _ in range(int(num_characters)))


with open("password.txt", "w") as f:
    f.write(password)


print(Fore.GREEN + "Your password is: " + password + "\nIt has been saved in password.txt.")
print(Fore.RESET)


print(Fore.YELLOW + "Do you want to copy it to the clipboard ? (y/n)")
clipboard = input().lower()

if clipboard == "y":
    pyperclip.copy(password)
    print(Fore.GREEN + "Password copied to clipboard.")
    print(Fore.RESET)
else:
    print(Fore.RED + "Password not copied to clipboard.")
    print(Fore.RESET)