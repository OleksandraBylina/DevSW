while True:
    a=(input())
    if a=="досить":
        break
    else:
        b=int(a)
strawberry=0
raspberry=0
blueberry=0
if b>9:
    raise RuntimeError
    strawberry+=1
elif b<0:
    raise TypeError
    raspberry+=1
elif b>=0 and b<=9:
    raise ValueError
    blueberry+=1
print (strawberry)
print (raspberry)
print(blueberry)



