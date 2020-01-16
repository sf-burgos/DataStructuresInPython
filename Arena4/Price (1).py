from sys import stdin as a
def monedas(n,m):
    global memoria
    if memoria[n][m]==None:
        if m==0:
            flag=0
        elif n==0:
            flag=1
        elif n<m:
            flag=monedas(n,m-1)
        else:
            flag=monedas(n-m,m)+monedas(n,m-1)
        memoria[n][m]=flag
    return memoria[n][m]
    
def main():
    global memoria
    memoria=[[None]*1002 for i in range(1003)]
    lista=[int(c)for c in a.readline().strip().split()]
    while lista!=[]:
        if len(lista)==3:
            num1,num2,num3=lista[0],lista[1],lista[2]
            if num1==0 and num2!=0:
                print(0)
            elif num1==0 and num2==0:
                print(1)
            else:
                if num2!=0:
                    ans=monedas(num1,num3)-monedas(num1,num2-1)
                    print(ans)
                else:
                    ans=monedas(num1,num3)
                    print(ans)
        elif len(lista)==2:
            num1,num2=lista[0],lista[1]
            if num1==0 and num2==0:
                print(1)
            else:
                ans=monedas(num1,num2)
                print(ans)
        else:
            num1=lista[0]
            if num1==0:
                print(1)
            else:
                ans=monedas(num1,num1)
                print(ans)
        lista=[int(c)for c in a.readline().strip().split()]
main()
