from sys import stdin

def main():
    m,n=[int(x) for x in stdin.readline().strip().split()]
    for i in range(m):
        lista=[int(x) for x in stdin.readline().strip().split()]
        for i in range(len(lista)):
            if lista[0]==2:
                print(*lista)
                po=True
                break
            elif lista[i]==2:
                u=sorted(lista[0:i])
                p=lista[i::]
                print(*u+p)
                po=True
                break
        if not p:
            print(*lista)

                
        
main()
