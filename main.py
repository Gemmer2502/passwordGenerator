from colorama import Fore
import random


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


print("How many characters do you want ?")
num_characters = int(input())

print("Do you want only number (1), only letter (2), both (3), number and special characters (4), letter and special characters (5), all (6) ?")
choice = int(input())

if choice == 1:
    characters = "0123456789"
    password = ''.join(random.choice(characters) for _ in range(num_characters))
elif choice == 2:
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ''.join(random.choice(characters) for _ in range(num_characters))
elif choice == 3:
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ''.join(random.choice(characters) for _ in range(num_characters))
elif choice == 4:
    characters = "0123456789!@#$%^&*()-+"
    password = ''.join(random.choice(characters) for _ in range(num_characters))
elif choice == 5:
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+"
    password = ''.join(random.choice(characters) for _ in range(num_characters))
elif choice == 6:
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+"
    password = ''.join(random.choice(characters) for _ in range(num_characters))


with open("password.txt", "w") as f:
    f.write(password)


print(Fore.GREEN + "Your password is: " + password + "\nIt has been saved in password.txt")
print(Fore.RESET)