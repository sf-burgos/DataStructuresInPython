from sys import stdin
def main():
    n=str(stdin.readline().strip())
    while n!="":
        n=int(n)
        c=int(stdin.readline().strip())
        print(p(n,c,1))
        n=str(stdin.readline().strip())

def p (n,k,i):
    if n-(i**k)==0:
        return 1
    elif n-(i**k)<0:
        return 0
    else:
        return p(n-i**k,k,i+1)+p(n,k,i+1)
        
main()
