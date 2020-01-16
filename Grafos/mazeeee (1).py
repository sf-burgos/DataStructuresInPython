from sys import stdin
import heapq
from collections import deque 
def main():
    a=int(stdin.readline().strip())
    for k in range(a):
        n=int(stdin.readline().strip())
        m=int(stdin.readline().strip())
        mat=[]
        for i in range(n):
            fila=[int(x) for x in stdin.readline().strip().split()]
            mat.append(fila)
        dis=[[float('inf')for x in range(m)]for y in range(n)]
        vis=[[False for x in range(m)]for y in range(n)]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        q=[]
        dis[0][0]=mat[0][0]
        heapq.heappush(q,(dis[0][0],0,0))
        while q:
            w,x1,y1=heapq.heappop(q)
            for x in range(4):
                if x1+dx[x]>=0 and x1+dx[x]<n and y1+dy[x]>=0 and y1+dy[x]<m:
                    if vis[x1+dx[x]][y1+dy[x]]==False:
                        if dis[x1+dx[x]][y1+dy[x]]>dis[x1][y1]+mat[x1+dx[x]][y1+dy[x]]:
                            dis[x1+dx[x]][y1+dy[x]]=dis[x1][y1]+mat[x1+dx[x]][y1+dy[x]]
                            heapq.heappush(q,(dis[x1+dx[x]][y1+dy[x]],x1+dx[x],y1+dy[x]))

            vis[x1][y1]=True
        print(dis[n-1][m-1])

main()
                    
            
        
        
            
            
        
        
    
