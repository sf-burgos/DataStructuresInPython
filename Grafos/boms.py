from sys import stdin

def main():
    global r,c
    r,c=[int(c) for c in stdin.readline().strip().split()]
    vertices=[]
    for i in range(r):
        for j in range(c):
            vertices.append((i,j))
    print(vertices)
    n=int(stdin.readline().strip())
    visitados=[]
    for i in range(n):
        lista=[int(c) for c in stdin.readline().strip().split()]
        row=lista[0]
        bombas=lista[2::]
        for bom in range(len(bombas)):
            visitados.append((row,bombas[bom]))
    
    print(visitados)
    l=[int(c) for c in stdin.readline().strip().split()]
    inicio=[int(c) for c in stdin.readline().strip().split()]
    fin=[int(c) for c in stdin.readline().strip().split()]
    create(vertices)
def create(visitados):
    global r,c
    graf={}
    for i in range(len(visitados)):
        graf[i]=[]
        a,b,c,d=i-1,i+1,i-r,i+r
        print(a,b,c,d)
        print(r,"llllll")
        if 0<=a<=(r):
            graf[i].append(a)
        if 0<=b<=(r):
            graf[i].append(b)
        if 0<=c<=(r):
            graf[i].append(c)
        if 0<=d<=(r):
            graf[i].append(d)
    
        
            
            
    print(graf)
main()
