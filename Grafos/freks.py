from sys import stdin


def make_set(x):
    global padre,rango
    padre[x]=x
    rango[x]=0

def find(x):
    global padre
    if padre[x]==x:
        return x
    else:
        padre[x]=find(padre[x])
        return padre[x]

def union(x,y):
    global rango,padre
    rx=find(x)
    ry=find(y)
    if rx!=ry:
        if rango[rx]< rango[ry]:
            padre[rx]=ry
        else:
            padre[ry]=rx
            if rango[rx]==rango[ry]:
                rango[rx]+=1

def kruskall():
    return False

def distancia (x2,x1,y2,y1):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def main():
    global padre,rango,ady,num
    n=int(stdin.readline().strip()) 
  
    for i in range(n):
        
        padre, rango = {}, {}
        vertice=[]
        dic={}
        c=0
        edges=[]
        k1=stdin.readline().strip()
        num=int(stdin.readline().strip())
        for j in range(int(num)):
            
            l=[float(c) for c in stdin.readline().strip().split()]
            l=tuple(l)
            vertice.append(l)
            dic[l]=j
        ady=[]
        for t in range (len(vertice)):
            for k in range (len(vertice)):
                if t<k or t==k:
                    pass
                else:
                    r=distancia(vertice[t][0],vertice[k][0],vertice[t][1],vertice[k][1])
                    g=(r,dic[vertice[t]],dic[vertice[k]])
                    if g not in ady:
                        ady.append(g)
        #print(ady)
        ady=sorted(ady)
        #print(ady)
        #print(vertice)
        
        for vertex in range (0,len(vertice)):
            make_set(vertex)
        
        total_weight = 0
        
        T = []
        for edge in ady:
            w, u, v = edge
            if find(u) != find(v):
                union(u, v)
                total_weight += w
                T.append((u,v))
        



                
        print("%.2f" % total_weight)
       


                    
main()
