inp="ansaf"
val=127
print("char\tand\tand_hex\t   or\t\tor_hex\t  xor\t\txor_hex")
for i in inp:
    x=ord(i)
    print(i,
          "\t",repr(chr(x&val)),
          "\t",hex(x&val),
          "\t",repr(chr(x|val)),
          "\t",hex(x|val),
          "\t",repr(chr(x^val)),
          "\t",hex(x^val)  
        )
    