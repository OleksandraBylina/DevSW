with open("exam_file") as fily:
    fily="".join(fily)
    pust=[]
    def recurse(fily):
        for el in fily:
            if el>0:
                pust.append(el)
            for el in pust:
                if pust[el]>pust[el-1]:
                    biggest=pust[el]
                    return biggest
                if pust[el]==None:
                    return (0)

