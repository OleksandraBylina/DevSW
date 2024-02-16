n=int(input())
spis = [int(i) for i in input().split()]
m=int(input())
spisko= [int(i) for i in input().split()]
pust=[]
for el in spis:
    if el not in spisko:
        pust.append(el)
print (len(pust))
print (*pust)