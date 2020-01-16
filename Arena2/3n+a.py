from sys import stdin
def main():
    c=[int(c) for c in stdin.readline().strip().split()]
    while c!=[]:
        a,b=c[0],c[1]
        lista=[]
        d,w=min(a,b),max(a,b)
        for i in range(d,w+1):
            o=i
            cont=1
            while o!=1:
                if o%2==0:
                    o=o/2
                    
                else:
                    o=3*o+1
                cont+=1
            lista.append(cont)
        print(str(a),str(b),max(lista))
        c=[int(c) for c in stdin.readline().strip().split()]   
        

main()
