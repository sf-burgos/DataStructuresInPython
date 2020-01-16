def create_set(n):
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
    #pi=padre de i
    #pj=padre de j   
    pi=find_set(i)
    pj=find_set(j)
    if pi!=pj:
        if rank[pi]<rank[pj]:
            pad[pi]=pj
        else:
            pad[pj]=pi
            if rank[pi]==rank[pj]:
                rank[pi]+=1
        return True
    return False
def kruskal(grafo):
    cont=0
    for arc in grafo:
        if union(arc[1],arc[2]):
            cont+=arc[0]
    return cont
def main():
    global pad,rank
    pad,rank={},{}
    n=3
    #n=cantidad de vertices del grafo
    for i in range(n):
        create_set(i)
    #grafo=lista de listas ordenada por costos
    grafo=[[4,0,1],[6,1,2],[9,2,0]]
    print(kruskal(grafo))
main()
