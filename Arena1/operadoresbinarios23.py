from sys import stdin

def winner(resp,i):
    # print(i)
    global entrada
    if i==len(entrada):
        # print("return ")
        if resp==23: return True
        else: return False
    else:
        i+=1
        a=winner(resp+entrada[i-1],i)
        b=winner(resp-entrada[i-1],i)
        c=winner(resp*entrada[i-1],i)
    if (a or b or c): return True 
    else: return False
def main():
    global entrada
    entrada=[int (xx) for xx in stdin.readline().strip().split(" ")]
    x=winner (entrada[0]+entrada[1],2)
    y=winner (entrada[0]-entrada[1],2)
    z=winner (entrada[0]*entrada[1],2)
    if (x or y or z):
        print("Possible")
    else:
        print("Impossible")
main()
