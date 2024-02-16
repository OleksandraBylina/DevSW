counter=0
pust=[]
for i in range (10000, 100001):
    destys=i//10000
    d=destys*10000
    du=i-d
    tys=du//1000
    tre=tys*1000
    tyu=du-tre
    sot=tyu//100
    desh=sot*100
    dede=tyu-desh
    des=dede//10
    od=dede%10
    if destys!=0:
        pust.append(destys)
    pust.append(tys)
    pust.append(sot)
    pust.append(des)
    pust.append(od)
    if pust==pust[::-1]:
        if i % 6 == 0:
            counter += 1
    pust=[]
print (counter)