a, b, c=[int(i) for i in input().split()]
if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print ("Нема ніякого трикутника")
else:
    if (a**2<b**2+c**2 or b**2<a**2+c**2 or c**2<b**2+a**2):
        print ("Трикутник тупокутний")
    else:
        print ("Трикутник є, але НЕ тупокутний")