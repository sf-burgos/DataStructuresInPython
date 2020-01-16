from sys import stdin
import decimal
import math
from collections import deque
""" GOPHER 2-10080 
Prtaentado por BRAYAN BURGOS DELGADO

PRE: El programa recibe 4 numeros denotados como n,m,s,v; donde n y m son el numero de castorta y agujeros rtapectivamente. Luego,
un tiempo dado en segundos y una velocidad dada en metros por segundo. Cada n y m tienen cordenadas cartesianas que se dan con un
espacio luego de los primeros 4 datos
POS: El numero de castorta que NO pueden ser salvados segun sea el caso 

"""
def distancia_p (x, y):
    """Pre: una lista de lista con x1, x2, y1, y2, osea 4 posiciones cartesianas del tipo (xsubn,ysubn) dadas por el problema
        pos: distancia euclidiana entre los las parejas cartesianas"""
    c=((x[0]-y[0])**2+(x[1]-y[1])** 2) 
    c=math.sqrt(c)
    return c
def increase (i,flow,c):
    """En teoría de grafos, una red de flujo es un grafo dirigido donde existen dos vértices especiales, uno llamado fuente,
    al que se le asocia un flujo positivo y otro llamado sumidero que tiene un flujo negativo y a cada arista se le asocia cierta
    capacidad positiva."""
    
    if i >= len(c):
        return flow
    else:
        x,y = c[i]
        flow[x][y] += 1
        increase(i+1,flow,c)
        
def bfs (flow,source,target):
    """Pre: El flujo por el cual estoy pasando en ese momento, lo dequeue dequeuiere decir
    es no perder la ruta y no visitar rutas no adecuadas
    Pos: si en caso no encontre un camino hasta el fin del grafo, retorna false
    si en cado caso SI llego al target, pues existe un camino seguro para llegar
    """
    
    global rta, n, m
    p = [[]for i in range(m+n+2)];deque = [];deque.append(source)
    visitados = [0 for i in range(m+n+2)]
    while deque:
        vertex = deque.pop(0)
        for v in range(m+n+2):
            #pilas con el flujo, tiene que ser mayor a 0 y no haberlo visitado nunca
            if not visitados[v] and (rta[vertex][v]-flow[vertex][v] > 0) :
                lineadeataque = p[vertex][:]
                lineadeataque.append((vertex,v))
                p[v] = lineadeataque
                visitados[v] = 1
                
                if v == target: return p[v]
                #agregar la v a la cola
                deque.append(v)
                
    return False
def  Ford_Fulkerson(flow_max):
    """propone buscar caminos en los que se pueda aumentar el flujo, hasta que se alcance el flujo máximo.
    Es aplicable a los Flujos maximales. La idea es encontrar una ruta de penetración con un flujo positivo neto
    que una los nodos origen y destino.
    Pre: Una lista de flujo maximal
    Pos: retorna el flujo maximo en el grafo, para donde en teoria son los gophers que se salvan en el transcurso del algoritmo
    """

    global n, m
    respuestaglobal = 0
    while True:
        c = bfs (flow_max,source,target)
        if not c: break
        increase (0,flow_max,c)
        respuestaglobal+=1
    return respuestaglobal




def main():
    global rta,n,m,s,v,source,target,flow_max
    """PRE: Ninguna
       POS: Funcion principal del problema, donde el MAX FLOW y el armado correcto del grafo para obtener la respuesta donde es la
       diferencia entre el algoritmo de flujos y n
    """
    ent=[int(c) for c in stdin.readline().strip().split()]
    while ent:
        n=ent[0];m=ent[1];s=ent[2];v=ent[3]
        distance=s*v;gophers=[];holes=[]
        #RTA BASICAMENTE ES EL GRAFO Y LE AGREGAMOS +2 para el SOURCE y EL TARGET que aconsejan todos
        rta=[[0 for i in range (n + m + 2)] for j in range (n + m + 2)]
        #matriz de n*m
        for i in range(n):
            gophers.append ([float (x) for x in stdin.readline().strip().split()])
            rta [0][i+1] = 1
        source=0;target=n+m+1;bandera=target+1
        for i in range(m):
            hol = [float (x) for x in stdin.readline().strip().split()]
            rta[n+i+1][-1] = 1
            for j in range(n):
                k=gophers[j]
                if distance>=distancia_p(hol,k):
                    rta[j+1][i+n+1]=1
                    
        flow_max = [[0 for j in range(n+m+2)]for i in range(n+m+2)]
        #esta la hago para realizar un cambio dinamico de en el flujo maximal, para alcanzar la ruta de penetracion con flujo maximo 
##        F=Ford_Fulkerson(flow_max)
##        print(F)
        salida=n-Ford_Fulkerson(flow_max)
        print(salida)
        ent=[int(c) for c in stdin.readline().strip().split()]
        
main()
#__________________________________________________________________________________________________________________________________-
##""" GOPHER 2-10080 
##Presentado por BRAYAN BURGOS DELGADO
##
##PRE: El programa recibe 4 numeros denotados como n,m,s,v; donde n y m son el numero de castores y agujeros respectivamente. Luego,
##un tiempo dado en segundos y una velocidad dada en metros por segundo. Cada n y m tienen cordenadas cartesianas que se dan con un
##espacio luego de los primeros 4 datos
##POS: El numero de castores que NO pueden ser salvados segun sea el caso 
##
##"""
##"""
##from sys import stdin
##import decimal
##
##def main():
##    """PRE: Ninguna
##       POS: Funcion principal del problema, donde el MAX FLOW y el armado correcto del grafo para obtener la respuesta 
##    """
##    global s,v
##    n,m,s,v=[int(c) for c in stdin.readline().strip().split()]
##    k=s*v; print(k)
##    gophers=[]
##    holes=[]
##    for i in range(n):
##        a=tuple(stdin.readline().strip().split())
##        gophers.append(a)
##    for j in range(n):
##        b=tuple(stdin.readline().strip().split())
##        holes.append(b)
##
##    print(gophers)
##    print(holes)
##    posibles=[]
##    #Distancias     
##    for gop in range(len(gophers)):
##        for hol in range(len(holes)):
##            r=distancia(float(gophers[gop][0]), float(holes[hol][0]),float(gophers[gop][1]), float(holes[hol][1]))
##            if r:
##                posibles.append((gophers[gop], holes[hol]))
##    mapeo(posibles)
##
##def distancia (x2,x1,y2,y1):
##
##    global s,v
##    resul=((x2-x1)**2+(y2-y1)**2)**0.5
##    print(resul)
##    if resul<=s*v:
##        return True
##    else:
##        return False
##
##def mapeo(posibles):
##    dic={}
##    for i in range(len(posibles)):
##        dic[posibles[i]]=i
##    print(dic)
##    
##
##def EdmondsKarp(E, C, s, t):
##    """PRE: C es la matriz de capacidades
##        E es la matriz de adyacencia
##        s es el source
##        t es sink
##       POS: retornara el flujo maximo del grafo 
##    """
##    n = len(C)
##    flow = 0
##    F = [[0 for y in range(n)] for x in range(n)]
##    while True:
##        P = [-1 for x in range(n)]
##        P[s] = -2
##        M = [0 for x in range(n)]
##        M[s] = decimal.Decimal('Infinity')
##        BFSq = []
##        BFSq.append(s)
##        pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
##        if pathFlow == 0:
##            break
##        flow = flow + pathFlow
##        v = t
##        while v != s:
##            u = P[v]
##            F[u][v] = F[u][v] + pathFlow
##            F[v][u] = F[v][u] - pathFlow
##            v = u
##    return flow
##
###https://brilliant.org/wiki/edmonds-karp-algorithm/
##
##def BFSEK(E, C, s, t, F, P, M, BFSq):
##    """PRE:
##       POS:
##    """
##    while (len(BFSq) > 0):
##        u = BFSq.pop(0)
##        for v in E[u]:
##            if C[u][v] - F[u][v] > 0 and P[v] == -1:
##                P[v] = u
##                M[v] = min(M[u], C[u][v] - F[u][v])
##                if v != t:
##                    BFSq.append(v)
##                else:
##                    return M[t], P
##    return 0, P
##main()"""
