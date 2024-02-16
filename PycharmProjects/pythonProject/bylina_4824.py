n=int(input())

def prostota(n):
     if n<2:
          return False
     for i in range(2, int(n**0.5)+1):
          if n%i==0:
               return False
          else:
               pass
     return True
def main(n, listy=[]):
     if n==1:
          return listy
     if prostota(n)==True:
          listy.append(n)
          return listy
     else:
          for m in range(2, n):
               if n%m==0:
                    listy.append(m)
                    return main(n//m)
print (main(n))





