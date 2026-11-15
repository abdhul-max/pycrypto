
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
key = os.urandom(32)
nonce = os.urandom(16)
data = b"Hello World!"
cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
encryptor = cipher.encryptor()
encrypted = encryptor.update(data)
decryptor = cipher.decryptor()
decrypted = decryptor.update(encrypted)
print("Original:", data.decode())
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted.decode())
if data == decrypted:
    print("Encryption Successful")

