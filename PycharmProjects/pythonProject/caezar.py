n=input()
m=int(input())
for i in n:
    i=ord(i)
    vert=i-m
    if vert<65:
        vert=91-(65-vert)

    print (chr(vert), end="")