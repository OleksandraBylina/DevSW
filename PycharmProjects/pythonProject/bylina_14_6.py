try:
    a, b, c=[int(i) for i in input().split()]
    def shuk(a, b, c):
        if b**2-4*a*c==0:
            vidp1=((-b)/(2*a))
        else:
            vidp1 = ((-b+((b**2-4*a*c)**(0.5)))/(2*a))
            vidp2 = (((-b-(b**2-4*a*c)**(0.5)))/(2*a))
        return (vidp1, vidp2)

    try:
        assert b**2-4*a*c>=0
        print(shuk(a, b, c))
    except AssertionError:
        print("Рівняння не має раціональних коренів(")
except ValueError:
    print ("Будь-ласка, введіть числове значення")



