from colorama import Fore
import pyperclip


def verify_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def error(text):
    print(Fore.RED + text)
    print(Fore.RESET)


def success(text):
    print(Fore.GREEN + text)
    print(Fore.RESET)


def information(text):
    print(Fore.YELLOW + text)
    print(Fore.RESET)


def greetings():
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


def clipboard(password):
    information("Do you want to copy the password to your clipboard? (y/n)")
    clipboard = input().lower()

    if clipboard == "y":
        pyperclip.copy(password)
        information("Password copied to clipboard.")
    else:
        information("Password not copied to clipboard.")


options = {
    1: "0123456789",
    2: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    3: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    4: "0123456789!@#$%^&*()-+?.,;",
    5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
    6: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+?.,;",
}