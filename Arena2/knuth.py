from sys import stdin



def main():
    s=str(stdin.readline().strip())
    while s!="":
        k(s,"" ,0)
        s=str(stdin.readline().strip())
def k(ori, cad, indicv):
    p=len(cad);o=len(ori)
    if p==o:
        print(cad)
    else:
        for cadaletra in range(len(cad)+1):
            w=cad[:cadaletra]+ori[indicv]+cad[cadaletra:]
            k(ori,w,indicv+1)
main()
