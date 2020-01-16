from sys import stdin
from collections import deque;import heapq
respuestas1 = [1,0,-1,0];respuestas2 = [0,1,0,-1]
def main():
    global respuestas1, respuestas2
    kl=float ('inf')
    c = int(stdin.readline().strip())
    while True:
       
        if c==0: break
        n = int(stdin.readline().strip())
        m = int(stdin.readline().strip())
        lr2 = []
        for i in range (n):
            fur = [int (x) for x in stdin.readline().strip().split()]
            lr2.append (fur)
        deque = []
        d = [[kl for x in range (m)]for y in range (n)]
        ady = [[0 for x in range (m)]for y in range (n)]
        #inicializar la lista de respuestas 2
        d[0][0] = lr2[0][0]
        heapq.heappush (deque,(d[0][0],0,0))
        while deque:
            w, x1, y1 = heapq.heappop(deque)
            cota=4
            #pilas con la cota
            for x in range (cota):
                if (x1 + respuestas1[x] >= 0) and (x1 + respuestas1[x] <n) and (y1 + respuestas2[x] >= 0) and (y1 + respuestas2[x] < m):
                    if ady[x1 + respuestas1[x]][y1 + respuestas2[x]] == 0:
                        if d[x1 + respuestas1[x]][y1 + respuestas2[x]] > d[x1][y1] + lr2[x1 + respuestas1[x]][y1 + respuestas2[x]]:
                            d[x1 + respuestas1[x]][y1 + respuestas2[x]] = d[x1][y1] + lr2[x1 + respuestas1[x]][y1 + respuestas2[x]]
                            heapq.heappush(deque,(d[x1 + respuestas1[x]][y1 + respuestas2[x]], x1 + respuestas1[x], y1 + respuestas2[x]))
            
            ady[x1][y1] = str(1)
        rta=d[n - 1][m - 1]
        print(rta)
        c=c-1

main()
                    
            
        
        
            
            
        
        
    
