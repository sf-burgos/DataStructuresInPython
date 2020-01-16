from sys import stdin



def make_set(v):
    global pad,ran
    pad[v],ran[v] = v,0

def find(v):
    global pad
    if v == pad[v]:
        return v
    else:
        pad[v] = find(pad[v])
        return pad[v]

def union(v1,v2):
    global pad,dis
    
    rv1 = find(v1)
    rv2 = find(v2)

    if rv1 != rv2:
        if ran[rv1] < ran[rv2]:
            pad[rv1] = rv2
        else:
            pad[rv2] = rv1
            if ran[rv1] == ran[rv2]:
                ran[rv1] += 1
        

def Kruskal(grafo):
    global pad,ran
    print(grafo)
    ran = dict()
    pad = dict()

    
    A = set()
    for v in grafo:          #para cada vertice. Hacer un make set
        make_set(v)
    print(A)
    #es posible sacar los arcos con una funcion auxiliar dependiendo del problema

    for edge in edges: #para cada arco
        #edge = (dis,v1,v2)
        dis,vertice1,vertice2 = edge[0],edge[1],edge[2]
        if find(vertice1) != find(vertice2):
            A.add(dis)
            union(vertice1,vertice2)
    return A

def distancia (x2,x1,y2,y1):
    return round(((x2-x1)**2+(y2-y1)**2)**0.5,2)

def main():
    global p 
    n=int(stdin.readline().strip())
    
    for i in range(n):
        k1=stdin.readline().strip()
        k=stdin.readline().strip()
        p=[]
        dic={}
        c=0
        for j in range(int(k)):
            l=[float(c) for c in stdin.readline().strip().split()]
            l=tuple(l); p.append(l)
            if l not in dic:
                dic[l]=c
                c+=1
                
        ady=[]
        for i in range(len(p)):
            for k in range(len(p)):
                if i!=k:
##                    print(p[i],p[k])
                    r=distancia(p[i][0],p[k][0],p[i][1],p[k][1])
##                    print(p[i],p[k],r)
                    #ff=sum(lista,key=lambda key: key[2])
                    a=min(dic[p[i]],dic[p[k]])
                    b=max(dic[p[i]],dic[p[k]])
                    rut=(r,a,b)
                    print(rut)
                    if rut not in ady:
                        ady.append(rut)
        print(Kruskal(ady))


                    
main()
