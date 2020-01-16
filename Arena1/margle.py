from sys import stdin
import bisect
def main():
    c=1
    a,b=[int(d) for d in stdin.readline().strip().split()]
    while a!=0 or b!=0:
        
        print("CASE#",str(c)+str(":"))
        lista=[]
        lista2=[]
        for i in range(a):
            l=int(stdin.readline().strip())
            lista.append(l)
        for k in range(b):
            p=int(stdin.readline().strip())
            lista2.append(p)
        lista.sort()
        for i in range(len(lista2)):
            z=searchbinary(lista,lista2[i])
            if z==-1:
                print(str(lista2[i]),"not found")
            else:
                
                o=bisect.bisect_left(lista,lista2[i],0,len(lista))
                print(str(lista2[i]),"found at", str(o+1))
        c+=1        
        a,b=[int(d) for d in stdin.readline().strip().split()]
def searchbinary(lista,x):
	"""Pre: la lista debe estar ordenada
	pos devuelve la posicion del elemento buscado """

	izq= 0
	der=len(lista)-1	
	while izq<=der:
		medio=int((izq+der)/2)
		if lista[medio]==x:
			return medio
		elif lista[medio]>x:
			der=medio-1
		else:
			izq=medio+1
	return -1
main()
