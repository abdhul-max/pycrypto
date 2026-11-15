def ceaser_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            start=0
            if char.isupper():
                start=ord("A")
            elif char.islower():
                start=ord("a")
            result+=chr((ord(char)-start+shift)%26+start)
        result+=char
    return result

text="abcdefg"
shift=1
mode=input("enter mode")
if mode==1:
    print(ceaser_cipher(text,shift))
else:
    print(ceaser_cipher(text,-shift))
