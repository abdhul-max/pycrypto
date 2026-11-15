
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
key=b"mysecretkey12345"
data=b"Hello World"
iv=get_random_bytes(Blowfish.block_size)
cipher=Blowfish.new(key,Blowfish.MODE_CBC,iv)
encrypted=cipher.encrypt(pad(data,Blowfish.block_size))
print("Plaintext:",data.decode())
print("IV:",iv.hex())
print("Encrypted:",encrypted.hex())
