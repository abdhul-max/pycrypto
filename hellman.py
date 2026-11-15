
from cryptography.hazmat.primitives.asymmetric import dh, ec
# Classical Diffie-Hellman
p = dh.generate_parameters(generator=2, key_size=2048)
a = p.generate_private_key()
b = p.generate_private_key()
s1 = a.exchange(b.public_key())
s2 = b.exchange(a.public_key())
print("DH Match:", s1 == s2)
print("Alice:", s1[:16].hex())
print("Bob:", s2[:16].hex())

# Elliptic Curve Diffie-Hellman
a = ec.generate_private_key(ec.SECP384R1())
b = ec.generate_private_key(ec.SECP384R1())
s1 = a.exchange(ec.ECDH(), b.public_key())
s2 = b.exchange(ec.ECDH(), a.public_key())
print("ECDH Match:", s1 == s2)
print("Alice:", s1[:16].hex())
print("Bob:", s2[:16].hex())
