n=input()
m=int(input())
for el in n:
    nomer=ord(el)-m
    if nomer<65:
        nomer=(91-(65-nomer))
    print (chr(nomer))