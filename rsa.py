
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
private=rsa.generate_private_key(public_exponent=65537, key_size=2048)
public=private.public_key()
msg=b"RSA Lab Message"
oaep=padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=None)
pss=padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH)
cipher=public.encrypt(msg,oaep)
decrypted=private.decrypt(cipher,oaep)
signature=private.sign(msg,pss,hashes.SHA256())
try:
    public.verify(signature,msg,pss,hashes.SHA256())
    verified=True
except Exception:
    verified=False
print("Original:",msg.decode())
print("Decrypted:",decrypted.decode())
print("Sign Verified:",verified)
