from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\x9e\xe3\xce\xb3g:}\xcdXO\xbd~\xb5\x13\x11\xa5?v\xd3\x17\xe2\x1b\xba\x9a0m\x8bu3/u5'

num = 1111

password = f"{num}"

key = PBKDF2(password, salt, dkLen=32)

message = b"luhlekhumalo"

cipher = AES.new(key, AES.MODE_CBC)

ciphered_data = cipher.encrypt(pad(message, AES.block_size))


with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    dencrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)


original = unpad(cipher.decrypt(dencrypt_data), AES.block_size)

print(original)