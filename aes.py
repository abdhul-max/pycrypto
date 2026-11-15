
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
data=b"Secret message"
key=get_random_bytes(16)
cipher=AES.new(key,AES.MODE_CBC)
iv=cipher.iv
encrypted=cipher.encrypt(pad(data,AES.block_size))
cipher=AES.new(key,AES.MODE_CBC,iv)
decrypted=unpad(cipher.decrypt(encrypted),AES.block_size)
print("Encrypted:",encrypted.hex())
print("Decrypted:",decrypted.decode())
