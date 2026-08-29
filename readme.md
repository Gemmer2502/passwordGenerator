# 🔐 Password Generator

A simple **password generator and encrypted password manager** built with Python.

This project was created as a personal project to practice Python.

## ✨ Features

* 🔑 Generate random passwords using Python's `secrets` module
* 📏 Choose the password length
* 🔤 Choose which characters to use:

  * Numbers only
  * Letters only
  * Letters + numbers
  * Numbers + special characters
  * Letters + special characters
  * Letters + numbers + special characters
* 🔒 Encrypt generated passwords before storing them
* 🗝️ Protect stored passwords with a master password
* 💾 Store encrypted passwords in `passwords.enc`
* 📋 Copy generated passwords directly to the clipboard
* 📖 Retrieve and decrypt previously saved passwords

## 🛠️ Technologies

* **Python**
* `secrets` — secure random password generation
* `cryptography` — encryption and key derivation
* `Argon2id` — deriving an encryption key from the master password
* `Fernet` — encrypting stored passwords
* `pyperclip` — clipboard management
* `colorama` — colored terminal output

## 📦 Installation

### 1. Clone the repository

```bash
git clone git@github.com:Gemmer2502/passwordGenerator.git
cd passwordGenerator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
source .venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Start the program with:

```bash
python main.py
```

The program will ask for your **master password** when it starts.

You can then choose between three options:

```text
1. See your saved passwords
2. Create a new password
3. Leave
```

### Generate a password

Choose option `2`.

You will be asked:

1. How many characters the password should contain
2. Which type of characters to use
3. Which service the password is for

The generated password is displayed in the terminal and encrypted before being saved to `passwords.enc`.

You can also choose to copy the password directly to your clipboard.

### View saved passwords

Choose option `1`.

The program decrypts the entries stored in `passwords.enc` using your master password and displays them.

## 🔐 How encryption works

When the program starts, it creates a random salt in `salt.txt` if one does not already exist.

The master password and this salt are used with **Argon2id** to derive a cryptographic key. That key is then used with **Fernet** to encrypt and decrypt the saved passwords.

The encrypted entries are stored in:

```text
passwords.enc
```

The salt is stored in:

```text
salt.txt
```

> ⚠️ **Important:** Do not lose your master password. The program relies on it to derive the key needed to decrypt your saved passwords.

## 📁 Project files

```text
passwordGenerator/
├── main.py
├── requirements.txt
├── salt.txt
├── passwords.enc
└── README.md
```

`passwords.enc` and `salt.txt` are generated/used by the application and should generally **not be committed to a public repository**.

## 📄 License

This project is mainly intended as a personal learning project.

P.S. this readme is from chatgpt because I didn't know what to say :)