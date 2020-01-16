from sys import stdin
def main():
    n=int(stdin.readline().strip())
    s=str(stdin.readline().strip())
    for i in range(n):
        print("Case #"+str(i+1)+str(":"))
        
        lista=[str(d) for d in stdin.readline().strip().split()]
        while lista!=[]:
            f=funtion(lista)
            print(f)
            lista=[str(d) for d in stdin.readline().strip().split()]
        print("")

def funtion(l):
    z=""
    cont=0
    c=0
    while c!=len(l):
        if len(l[c])>cont:
            z+=l[c][cont]
            c+=1
            cont+=1
        else:
            c+=1
    return z

main()
