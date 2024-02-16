n = [int(i) for i in input().split()]
def alfa(n):
    counter=0
    q=0
    while True:
        try:
            kostya=(n[q])
            q+=1
            counter+=1
        except IndexError:
            break
    return (counter)
print (alfa(n))
def beta(n):
    counter = 0
    q = 0
    while True:
        try:
            bone = (n[q])
            q += 1
            counter += bone
        except IndexError:
            break
    return (counter)
print (beta(n))
def gamma(n):
    if max(n)>=0 and min(n)>=0:
        try:
            zeba=max(n)/min(n)
        except ZeroDivisionError:
            n.remove(0)
            zeba=max(n)/min(n)
        return (zeba)
print ((gamma(n)))
