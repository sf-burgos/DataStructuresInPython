from sys import stdin
def main():
    m,n=[int(s) for s in stdin.readline().strip().split()]
    for i in range(m):
        lista=[int(c) for c in stdin.readline().strip().split()]
        g=l(lista)
        print(*g)

def l (lista):
    p=False
    if lista[0]==2:
        return lista
    for i in range(len(lista)):
        if lista[i]==2:
            lista=sorted(lista[0:i])+lista[i:]
            p=True
            break
    if not p:
        lista=sorted(lista)
    return lista



main()
