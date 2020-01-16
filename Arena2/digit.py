from sys import stdin
def main():
    l=[str(c) for c in stdin.readline().strip().split()]
    while l!=[]:
        n=list(l[0]);k=int(l[1])
        n=n*k

        n=digit(n)
        while len(n)>1:
            n=digit(n)
        print(int(n[0]))
        l=[str(c) for c in stdin.readline().strip().split()]












def digit(lista):
    for i in range(len(lista)):
        lista [i]=int(lista[i])
    lista=list(str(sum(lista)))
    return lista
main()
