from sys import stdin
def main():
        inicio=[str(y) for y in stdin.readline().strip().split()]
        while inicio!=[]:
            lon,cad=inicio[0],inicio[1]
            lon2,cad2=[str(c) for c in stdin.readline().strip().split()]







            

            matriz=[[0 for i in range (int(lon)+1)] for j in range(int(lon2)+1)]
        

            for i in range(1,int(lon)+1):
                matriz[0][i]=i
            for j in range(1,int(lon2)+1):
                matriz[j][0]=j


            #for i in matriz:
                #print(i)
            #print("_____________________________________________")

            for k in range(1,int(lon2)+1):
                for y in range(1,int(lon)+1):
                    if cad[y-1]!=cad2[k-1]:
                        matriz[k][y]=min(1+matriz[k-1][y-1],1+matriz[k][y-1],1+matriz[k-1][y])
                    else:
                        matriz[k][y]=matriz[k-1][y-1]







            print(matriz[-1][-1])

            inicio=[str(y) for y in stdin.readline().strip().split()]

    




















main()








   










