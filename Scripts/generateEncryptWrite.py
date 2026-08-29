import secrets
from fonctionVariableAndDictionnary import error, verify_int, options


def generate_password():
    while True:
        print("How many characters do you want ?")
        numCharacters = input()

        if verify_int(numCharacters) == False or int(numCharacters) <= 0:
            error("Must be a number higher than 0.")
        else:
            numCharacters = int(numCharacters)
            break


    while True:
        print("Do you want only number (1), only letter (2), both (3), number and special characters (4), letter and special characters (5), all (6) ?")
        typeCharacters = input()

        if verify_int(typeCharacters) == False or int(typeCharacters) < 1 or int(typeCharacters) > 6:
            error("Must be a number between 1 and 6.")
        else:
            typeCharacters = int(typeCharacters)
            break


    characters = options.get(typeCharacters)

    password = ''.join(secrets.choice(characters) for _ in range(numCharacters))
    return password


def write_encryptedPassword(f, serviceAndPass):
    with open("passwords.enc", "ab") as passFile:
        passFile.write(f.encrypt((serviceAndPass).encode()) + b"\n")