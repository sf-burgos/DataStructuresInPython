from sys import stdin

def main():
    entrada = [i for i in stdin.readline().strip().split()]
    while len(entrada) != 0:
    
        m = int(entrada[0])
        n = int(entrada[1])
        t = int(entrada[2])
        A = [-1 for x in range(20001)]
        oo = A[0]
        A[0] = 0
        tt = t - min(n,m)
        for i in range(tt+1):
            if A[i] != oo:
                A[i+m] = max(A[i+m], A[i]+1)
                A[i+n] = max(A[i+n], A[i]+1)
        s = t
        while A[s] == oo:
            s = s-1
        if s == t:
            print(A[s])
        else:
            print(A[s],(t-s))

        entrada = [i for i in stdin.readline().strip().split()]
main()


    
