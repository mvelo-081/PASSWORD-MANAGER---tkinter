# Password Manager App

A secure and user-friendly **Password Manager** built with **Python** and the **Tkinter GUI library**. This app allows users to generate, encrypt, store, and retrieve strong passwords locally — without storing any master password on disk.

## Features

- **Account System**: Users create an account with a master password (used for encryption/decryption).
- **Secure Password Generation**: Automatically generates strong, unhackable passwords.
- **Local Encryption**: All passwords are encrypted and stored locally in a `.txt` file.
- **Decryption on Demand**: Users can retrieve their passwords by entering their master password and account name.
- **Master Password is Never Stored**: User credentials are not stored anywhere to improve security.
- **In-Progress**: Integration of **AES encryption with salt** to enhance local security of stored data.

## Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Cryptography / hashlib** for encryption
- **Object-Oriented Programming** for modular and maintainable code

## What I Learned

This project helped me:
- Understand **secure local storage** and encryption techniques
- Implement **object-oriented design patterns** in GUI development
- Manage **user authentication flows** without exposing credentials
- Work with **file handling** and **symmetric encryption**

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
