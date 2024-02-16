kostya=0
pust=[]
n=0
with open("1") as fily:
    dlinna=fily.readline()
    for i in range(int(dlinna)):
        am=fily.readline()
        am=am.split()
        if len(am)!=int(dlinna):
            kostya=1
        

if kostya==1:
    print ("Хрень, переделывай")

#def sovp(fily):




