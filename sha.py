
import hashlib, os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
data = b"Verify my integrity statement"
print("SHA-256:", hashlib.sha256(data).hexdigest())
print("SHA-3:", hashlib.sha3_256(data).hexdigest())
password = b"SuperSecurePassword123"
salt=os.urandom(16)
kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32, salt=salt, iterations=100000)
key=kdf.derive(password)
print("Salt:", salt.hex())
print("PBKDF2 Key:", key.hex())




import hashlib
import os
data = b"Verify my integrity statement"
print("SHA-256:",hashlib.sha256(data).hexdigest())
print("SHA-3:",hashlib.sha3_256(data).hexdigest())
password=b"SuperSecurePassword123"
salt=os.urandom(16)
key=hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
print("Salt:",salt.hex())
print("PBKDF2 Key:",key.hex())
