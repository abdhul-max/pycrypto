
def hill(text, mode):
    k=[[3,3],[2,5]]
    res=""
    text=text.upper()
    if len(text)%2:
        text+="X"
    for i in range(0,len(text),2):
        a,b=ord(text[i])-65,ord(text[i+1])-65
        if mode=="encrypt":
            x,y=(3*a+3*b)%26, (2*a+5*b)%26
        else:
            x,y=(15*a+17*b)%26, (20*a+9*b)%26
        res+=chr(x+65)+chr(y+65)

    return res
text=input("Text:")
mode=input("Mode:")
print(hill(text,mode))
