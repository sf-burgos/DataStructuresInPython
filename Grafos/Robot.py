from sys import stdin
from collections import deque
def main():
    global lista,a,b
    while True:
        a,b,c=[int(c) for c in stdin.readline().strip().split()]
        if a==b==c==0: break      
        lista=[]
        for i in range(a):
            s=str(stdin.readline().strip())
            lista.append(s)
        BFS((0,c-1))

def BFS(inicial):
    global lista,a,b

    
    s=deque();u=set();s.append(inicial);u.add(inicial)
    bandera=False
    d=[]
    d.append(inicial)
    n=0
    while len(s):
        p=s.popleft()
        if p[0]==0 and lista[p[0]][p[1]]=="N": break
        elif p[0]==a-1 and lista[p[0]][p[1]]=="S": break
        elif p[1]==0 and lista[p[0]][p[1]]=="W": break
        elif p[1]==b-1 and lista[p[0]][p[1]]=="E": break
        else:
            if lista[p[0]][p[1]]=="W":
                o=(p[0],p[1]-1)
            elif lista[p[0]][p[1]]=="S":
                o=(p[0]+1,p[1])
            elif lista[p[0]][p[1]]=="E":
                o=(p[0],p[1]+1)
            elif lista[p[0]][p[1]]=="N":
                o=(p[0]-1,p[1])
            if o not in u:
                u.add(o)
                s.append(o)
                d.append(o)
            else:
                n=d.index(o)
                bandera=True
            
    
    if bandera:
        print(n,"step(s) before a loop of",len(u)-n,"step(s)")
    else:
        print(len(u),"step(s) to exit")

    
main()
