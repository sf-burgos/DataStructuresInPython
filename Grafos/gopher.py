from sys import stdin
from collections import deque
def aumento (i,flow,camino):
    """avanza por todo el camino actualizando el flujo"""
    if i >= len(camino):
        return flow
    else:
        u,v = camino[i]
        flow[u][v] += 1
        aumento(i+1,flow,camino)
        
def busqueda (flow):
    global res, n, m, ini, fin
    #p va a guardar el camino por el cual llegue a cada nodo
    p = [[]for i in range(m+n+2)]
    q = []
    q.append(ini)
    visit = [0 for i in range(m+n+2)]
    while q!=[]:
        u = q.pop(0)
        for v in range(m+n+2):
            """si el flujo que pasa es mayor a 0 y
            no he visitado v en esta iteración avanza"""
            if res[u][v]-flow[u][v] > 0 and not visit[v]:
                line = p[u][:]
                line.append((u,v))
                p[v] = line
                visit[v] = 1
                #si llego al final retorno el camino por el cual llegue a el
                if v == fin:
                    return p[v]
                q.append(v)
    #si no encontre un camino hasta fin retorno falso
    return False

def algoritmo():
    global n, m
    mf = 0
    """se crea una matriz igual a el grafo con flujo 0"""
    flow = [[0 for j in range(n+m+2)]for i in range(n+m+2)]
    while True:
        camino = busqueda (flow)
        if not camino:
            break
        aumento (0,flow,camino)
        mf+=1
    return mf

def distancia (p, q):
    return ((p [0] - q [0]) ** 2 + (p [1] - q [1]) ** 2) ** 0.5

def main():
    global res, Vt, mf, f, n, m, p, ini, fin
    l = [int (x) for x in stdin.readline().strip().split()]
    while l:
        n, m, s, v = l
        res = [[0 for x in range (n + m + 2)] for y in range (n + m + 2)]
        x = s * v
        nutrias = []
        for i in range (n):
            nutrias.append ([float (x) for x in stdin.readline().strip().split()])
            res [0][i+1] = 1
        huecos = []
        ini = 0
        fin = n + m + 1
        Vt = fin + 1 
        for i in range (m):
            p = [float (x) for x in stdin.readline().strip().split()]
            res[n+i+1][-1] = 1
            for j in range (n):
                q = nutrias [j]
                if distancia (p, q) <= x:
                    res [j+1][i+n+1] = 1
        print (n - algoritmo())
        l = [int (x) for x in stdin.readline().strip().split()]
main()
