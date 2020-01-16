from sys import stdin as a
def dist(x1,x2,y1,y2):
    res=(((x2-x1)**2)+((y2-y1)**2))**0.5
    return res
def create(n):
    global pad,rank
    pad[n]=n
    rank[n]=1
def find_set(n):
    global pad,rank
    if pad[n]==n:
        return n
    else:
        return find_set(pad[n])
def union(i,j):
    global pad,rank
    pad_i=find_set(i)
    pad_j=find_set(j)
    if pad_i!=pad_j:
        if rank[pad_i]<rank[pad_j]:
            pad[pad_i]=pad_j
        else:
            pad[pad_j]=pad_i
            if rank[pad_i]==rank[pad_j]:
                rank[pad_i]+=1
        return True
    else:
        return False
def kruskal(ady):
    cont=0
    for nod in ady:
        if union(nod[1],nod[2]):
            cont+=nod[0]
    return cont
def main():
    global pad,rank
    num=int(a.readline().strip())
    while num>0:
        num-=1
        a.readline()
        dic={}
        pad={}
        rank={}
        nod=int(a.readline().strip())
        ady=[]
        for i in range(nod):
            create(i)
            x,y=[float(g)for g in a.readline().strip().split()]
            if i not in dic:
                dic[i]=(x,y)
        for t in range(nod):
            for h in  range(nod):
                if t<h or t==h:
                    pass
                else:
                    res=dist(dic[t][0],dic[h][0],dic[t][1],dic[h][1])
                    ady.append((res,t,h))
        ady=sorted(ady)
        print("{0:.2f}".format(kruskal(ady)))
        if num>0:
            print()
main()
