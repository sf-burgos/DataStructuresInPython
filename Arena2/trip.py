from sys import stdin
def main():
    n,m=[int(c) for c in stdin.readline().strip().split()]
    paradas=[]
    for i in range(n+1):
        l=int(stdin.readline().strip())
        paradas.append(l)
    cota_inferior=max(paradas)
    cota_superior=sum(paradas)
    busq=[int(c) for c in range(cota_inferior,cota_superior+1)]
   # print(busq)
    cont=m
    #print(paradas)
    w,y=simulation(busq,paradas,cont)
    print("------")
    print(w,y)

    
def simulation(busq,paradas,cont):
    print(cont)
    
    mitad=busq[0]+busq[-1]//2
   # print(mitad)
   # print(".....")
    for i in range(len(paradas)+1):
        var=sum(paradas[0:i])
        #print(paradas[0:i])
        #print(var,"v")
        if var>mitad:
            cont-=1
    z=(mitad,cont)
    return z










#print(simulation([int(c) for c in range (7,25)],[7,2,6,4,5],3))
main()
