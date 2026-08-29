from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
import os
import base64


def salt():
    if os.path.exists("Data/salt.txt"):
        with open("Data/salt.txt", "rb") as f:
            salt = f.read()
    else:
        salt = os.urandom(16)
        with open("Data/salt.txt", "wb") as f:
            f.write(salt)
    return salt

def settings():
    kdf = Argon2id(
        salt=salt(),
        length=32,
        iterations=3,
        lanes=4,
        memory_cost=128 * 1024
    )
    return kdf

def masterPassword_creationKey(kdf):
    print("What's your master password (a password that you need to remember that will be used to encrypt your password)")
    masterPassword = input()

    key = base64.urlsafe_b64encode(kdf.derive(masterPassword.encode()))
    f = Fernet(key)
    return f