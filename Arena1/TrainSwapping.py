from sys import stdin
def main():
    x=int(stdin.readline().strip())
    for i in range(x):
        o=int(stdin.readline().strip())
        lista=[int(c) for c in stdin.readline().strip().split()]
        cont=0
        p=bubbleSort(lista,cont)
        print("Optimal train swapping takes",str(p),"swaps.")




def bubbleSort(alist,cont):
    #print(alist)
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                cont+=1
    return cont


main()
