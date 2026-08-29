from fonctionVariableAndDictionnary import verify_int, error, information, success


def del_password(value):
    while True:
        print("Which password do you want to delete (say the number before the password)?")
        passDel = input()

        if verify_int(passDel) == False or int(passDel) < 0 or int(passDel) > (value - 1):
            error(f"Must be a number between 1 and {(value - 1)}.")
        else:
            passDel = int(passDel)
            print(f"Are you sur you want to delete password n°{passDel} (y/n)?")
            verification = input().lower()

            if verification != "y":
                information("Cancellation of deletion.")
                break
            else:
                numPass = 0
                lines_to_keep = []
                with open("Data/passwords.enc", "rb") as passFile:
                    for line in passFile:
                        if numPass != passDel:
                            lines_to_keep.append(line)
                        numPass += 1

                with open("Data/passwords.enc", "wb") as passFile:
                    for line in lines_to_keep:
                        passFile.write(line)

                success(f"Successfully deleted password n°{passDel}")
                break