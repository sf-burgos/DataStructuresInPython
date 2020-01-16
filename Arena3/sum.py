from sys import stdin
def main():
    lista=[int(T) for T in stdin.readline().strip().split()]
    while True:
        if lista==[0,0]:
            break
        else:
            A=lista[2::];cont=0;L=[]
            for i in range(len(A)):
                for j in range(len(A)):
                    for k in range(len(A)):
                    
                        if j<k and (i!=k) and (i!=j) and j!=k:
                            pivote=A[i];arr=A[0:j]+A[k+1::];arr2=A[j+1:k];s=sum(arr);u=sum(arr2)
                           
            
                            if s+pivote==lista[0]:
                                arr.append(pivote);w=sorted(arr)
                                
                                if w not in L:
                                    L.append(w);cont+=1
                                   
                            elif u+pivote==lista[0]:
                                arr2.append(pivote);u=sorted(arr2)
                                if u not in L:
                                    L.append(u);cont+=1
                                    
            print("Sums of",str(lista[0])+":")
            if cont==0: print("NONE")
            else: print(cont)
            lista=[int(T) for T in stdin.readline().strip().split()]
  




main()
