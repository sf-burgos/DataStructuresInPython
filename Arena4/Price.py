from sys import stdin 
def recurencia(n,m):
    global price
    #____________________
    if price[n][m]==-1:
        if m==0: banderin=0
        elif n==0: banderin=1
        elif n<m: banderin=recurencia(n,m-1)
        else:banderin=recurencia(n-m,m)+recurencia(n,m-1)
        price[n][m]=banderin
    return price[n][m]
    
def main():
    global price
    price=[[-1]*1002 for i in range(1003)];
    while True:
        push=[int(c)for c in stdin.readline().strip().split()]
        if push==[]: break
        if len(push)==3:
            a,b,c=push[0],push[1],push[2]
            if a==0 and b!=0: print("0")
            elif a==0 and b==0:print("1")
            else:
                if b!=0:
                    respuesta=recurencia(a,c)-recurencia(a,b-1)
                    print(str(respuesta))
                else:
                    respuesta=recurencia(a,c)
                    print(str(respuesta))
        #___________________________________________________________
        elif len(push)==2:
            a=push[0];b=push[1]
            if a==0 and b==0: print("1")
            else:
                respuesta=recurencia(a,b)
                print(respuesta)
        else:
            a=push[0]
            if a==0:
                print(1)
            else:
                respuesta=recurencia(a,a)
                print(respuesta)
main()
