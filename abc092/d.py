ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

A,B=rl()

# 0:.    1:#
def print_g(g, rev):
    if rev==0:
        if g==0:
            print('.',sep='',end='')
        else:
            print('#',sep='',end='')
    else:
        if g==0:
            print('#',sep='',end='')
        else:
            print('.',sep='',end='')


rev = 0
if A > B:
    A,B = B,A
    rev = 1

mw=0
mh=0
mcell = (A-1)*2

for i in range(99,1,-1):
    if mcell%i==0:
        mw = i
        mh = mcell // i
        break
    elif (mcell-1)%i==0:
        mw = i
        mh = (mcell-1) // i
        break

#print(mw)
#print(mh)
if mw*mh != 0:
    b_res = B - ((mw-1)*(mh-1)//2+1)
else:
    b_res = B - 1
#print(b_res)

print(100,100)
for h in range(1,101):
    for w in range(1,101):
        if h <= mh:
            if w <= mw:
                print_g((w-1)%2,rev)
            else:
                print_g(1,rev)
        elif h == mh+1:
            print_g(1,rev)
        else:
            if (h-(mh+1))%2 == 1:
                print_g(0,rev)
            else:
                if b_res > 0:
                    print_g(w%2,rev)
                    b_res -= 1 if w%2 else 0
                else:
                    print_g(0,rev)
    print()

            

    