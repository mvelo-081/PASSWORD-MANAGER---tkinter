from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_password(password):
    salt = get_random_bytes(32)
    key = PBKDF2(password , salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(b"hello world!", AES.block_size))
    return ciphered_data, key

def dencrypt_password(password):
    cipher = AES.new(key)
def save_to_file(encrypt_password):
    with open('mvelo.txt', 'a') as file:
        file.write(f"Mvelo:{encrypt_password}\n")
    
    
    
encrypt_password = encrypt_password('123456')
save_to_file(encrypt_password)

print(encrypt_password.key)