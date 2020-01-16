from sys import stdin
import bisect
def main():
    m,n=[int(c) for c in stdin.readline().strip().split()]
    for i in range(m):
        lista=[str(e) for e in stdin.readline().strip().split()]
        r=g(lista)
        print(*r)
def g(lista):
    principio,final=[],[]
    
    if "2" in lista:
        if lista[0]=="2":
            return lista
        else:
            y=bisect.bisect_left(lista,"2",0,len(lista)-1)
            #print(y)
            principio=lista[0:y]
            final=lista[y::]
            principio=sorted(principio)
            return principio+final
    else:
        lista=sorted(lista)
        return lista 

main()
