def sub(text,cipher,mode="encrypt"):
    res=""
    normal="abcdefghijklmnopqrstuvwxyz"
    text=text.lower()
    if mode=="encrypt":
        map={normal[i]:cipher[i] for i in range(26)}
    else:
        map={cipher[i]:normal[i] for i in range (26)}
    for char in text:
        if char.isalpha():
            res+=map[char]
        else:
            res+=char
    return res





