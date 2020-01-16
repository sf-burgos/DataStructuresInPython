from sys import stdin
def main():
    n,m,k=[int(i) for i in stdin.readline().strip().split()]
    z=n*m
    lista=[]
    for i in range(k):
        f,c1,c2=[int(i) for i in stdin.readline().strip().split()]
        for i in range(c1,c2+1):
            a=f,i
            if a not in lista:
                lista.append(a)
    print(abs(len(lista)-z))            


main()
