import os
from fonctionVariableAndDictionnary import error, success



def read_password(f):
    possible = True
    count = 0
    errorCount = 0
    if os.path.exists("Data/passwords.enc") == False:
        error("You don't have passwords")
        possible = False
    else:
        with open("Data/passwords.enc", "rb") as passFile:
            for line in passFile:
                try:
                    success(f"{count}) {f.decrypt(line).decode().strip()}")
                except:
                    errorCount += 1
                    error("For this password, this is not the good master password.")
                count += 1
            if count == errorCount:
                possible = False
    return possible, count