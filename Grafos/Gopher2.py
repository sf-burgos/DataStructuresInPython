""" GOPHER 2-10080 
Presentado por BRAYAN BURGOS DELGADO

PRE: El programa recibe 4 numeros denotados como n,m,s,v; donde n y m son el numero de castores y agujeros respectivamente. Luego,
un tiempo dado en segundos y una velocidad dada en metros por segundo. Cada n y m tienen cordenadas cartesianas que se dan con un
espacio luego de los primeros 4 datos
POS: El numero de castores que NO pueden ser salvados segun sea el caso 

"""

from sys import stdin
import decimal

def main():
    """PRE: Ninguna
       POS: Funcion principal del problema, donde el MAX FLOW y el armado correcto del grafo para obtener la respuesta 
    """
    global s,v
    n,m,s,v=[int(c) for c in stdin.readline().strip().split()]
    k=s*v; print(k)
    gophers=[]
    holes=[]
    for i in range(n):
        a=tuple(stdin.readline().strip().split())
        gophers.append(a)
    for j in range(n):
        b=tuple(stdin.readline().strip().split())
        holes.append(b)

    print(gophers)
    print(holes)
    posibles=[]
    #Distancias     
    for gop in range(len(gophers)):
        for hol in range(len(holes)):
            r=distancia(float(gophers[gop][0]), float(holes[hol][0]),float(gophers[gop][1]), float(holes[hol][1]))
            if r:
                posibles.append((gophers[gop], holes[hol]))
    mapeo(posibles)

def distancia (x2,x1,y2,y1):

    global s,v
    resul=((x2-x1)**2+(y2-y1)**2)**0.5
    print(resul)
    if resul<=s*v:
        return True
    else:
        return False

def mapeo(posibles):
    dic={}
    for i in range(len(posibles)):
        dic[posibles[i]]=i
    print(dic)
    

def EdmondsKarp(E, C, s, t):
    """PRE: C es la matriz de capacidades
        E es la matriz de adyacencia
        s es el source
        t es sink
       POS: retornara el flujo maximo del grafo 
    """
    n = len(C)
    flow = 0
    F = [[0 for y in range(n)] for x in range(n)]
    while True:
        P = [-1 for x in range(n)]
        P[s] = -2
        M = [0 for x in range(n)]
        M[s] = decimal.Decimal('Infinity')
        BFSq = []
        BFSq.append(s)
        pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
        if pathFlow == 0:
            break
        flow = flow + pathFlow
        v = t
        while v != s:
            u = P[v]
            F[u][v] = F[u][v] + pathFlow
            F[v][u] = F[v][u] - pathFlow
            v = u
    return flow

#https://brilliant.org/wiki/edmonds-karp-algorithm/

def BFSEK(E, C, s, t, F, P, M, BFSq):
    """PRE:
       POS:
    """
    while (len(BFSq) > 0):
        u = BFSq.pop(0)
        for v in E[u]:
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t:
                    BFSq.append(v)
                else:
                    return M[t], P
    return 0, P
main()
