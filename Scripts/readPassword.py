import os
from fonctionVariableAndDictionnary import error, success


def read_password(f):
    if os.path.exists("passwords.enc") == False:
        error("You don't have passwords")
    else:
        with open("passwords.enc", "rb") as passFile:
            for line in passFile:
                try:
                    success(f.decrypt(line).decode().strip())
                except ValueError:
                    error("For this password, this is not the good master password.")