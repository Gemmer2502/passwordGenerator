from fonctionVariableAndDictionnary import greetings, error, success, clipboard, verify_int, information
from settingsEncrypt import settings, masterPassword_creationKey
from generateEncryptWrite import generate_password, write_encryptedPassword
from readPassword import read_password
from deletePassword import del_password


greetings()

kdf = settings()

f = masterPassword_creationKey(kdf)


while True:
    print("Do you want to create a password (1), see your password (2) or exit (3)?")
    mode = input()

    
    if verify_int(mode) == False or int(mode) < 1 or int(mode) > 3:
        error("Must be a number between 1 and 3.")
    else:
        mode = int(mode)

        if mode == 1:
            password = generate_password()

            print("For what service will the password be used? (youtube, google, facebook...)")
            service = input()
            serviceAndPass = service + ": " + password

            success("Your password is: " + password + "\nIt has been saved in passwords.enc.")

            write_encryptedPassword(f, serviceAndPass)

            clipboard(password)

        elif mode == 2:
            possible, count = read_password(f)

            if possible:
                while True:
                    print("Do you want to delete a password (1), modify a password (2) or go back to the menu (3)?")
                    choice = input()

                    if verify_int(choice) == False or int(choice) < 1 or int(choice) > 3:
                        error("Must be a number between 1 and 3.")
                    else:
                        choice = int(choice)

                        if choice == 1:
                            del_password(count)

                        if choice == 2:
                            information("Mécanique a ajouter !")

                        if choice == 3:
                            break


        elif mode == 3:
            print("Goodbye.")
            break