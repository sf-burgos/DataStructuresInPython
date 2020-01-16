from sys import stdin;import heapq;from collections import deque 
def main():
    casos=int(stdin.readline().strip())
    while casos!=0:
        n=int(stdin.readline().strip());m=int(stdin.readline().strip())
        matriz=[]
        for i in range(n):
            fila=[int(x) for x in stdin.readline().strip().split()]
            matriz.append(fila)
        dis=[[float('inf')for x in range(m)]for y in range(n)]
        vis=[[False for x in range(m)]for y in range(n)]
        respuestas1=[1,0,-1,0];respuestas2=[0,1,0,-1];q=[]
        dis[0][0]=matriz[0][0]
        heapq.heappush(q,(dis[0][0],0,0))
        while q:
            w,x1,y1=heapq.heappop(q)
            for x in range(4):
                if x1+respuestas1[x]>=0 and x1+respuestas1[x]<n and y1+respuestas2[x]>=0 and y1+respuestas2[x]<m:
                    if vis[x1+respuestas1[x]][y1+respuestas2[x]]==False:
                        if dis[x1+respuestas1[x]][y1+respuestas2[x]]>dis[x1][y1]+matriz[x1+respuestas1[x]][y1+respuestas2[x]]:
                            dis[x1+respuestas1[x]][y1+respuestas2[x]]=dis[x1][y1]+matriz[x1+respuestas1[x]][y1+respuestas2[x]]
                            heapq.heappush(q,(dis[x1+respuestas1[x]][y1+respuestas2[x]],x1+respuestas1[x],y1+respuestas2[x]))

            vis[x1][y1]=1
        e=dis[n-1][m-1]
        print(e)
        casos=casos-1
main()
                    
            
        
        
            
            
        
        
    
