from sys import stdin 
def back_tracking(lis):
    global p;numerosprimos;conjunto
    if len(lis)==p:
        if lis[0]+lis[-1] in numerosprimos:
            print(" ".join(str(i)for i in lis))
    else:
        for v in range(2,p+1):
            if lis[-1]+v in numerosprimos and v not in conjunto:
                if v not in lis:
                    conjunto.add(v)
                    back_tracking(lis+[v])
                    conjunto.remove(v)
                else:
                    continue

def main():
    global p,numerosprimos,conjunto
    p=str(stdin.readline().strip())
    cont=1
    numerosprimos={1,2,3,5,7,11,13,17,19,23,29,31,37,41,43}
    while p != "":
        p=int(p);conjunto=set();lista=[1]
        if p%2==0:
            print("Case",str(cont)+":")
            back_tracking(lista)
            print()
        else:
            print("Case",str(cont)+":")
            print()
        cont+=1
        p=str(stdin.readline().strip())
main()
