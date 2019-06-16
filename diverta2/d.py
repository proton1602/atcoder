import sys
input = sys.stdin.readline
ri = lambda: int(input())
#rl = lambda: [int(x) if x.isdecimal() else x for x in input().split()]
#rl = lambda: list(input().split()))
rl = lambda: map(int,input().split())
rr = lambda N: [list(l) for l in zip(*[rl() for _ in range(N)])]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

N = ri()
ga,sa,ba = rl()
gb,sb,bb = rl()
G = int(ga>=gb)
S = int(sa>=sb)
B = int(ba>=bb)
GSB =G+S+B
xa,xb,ya,yb,za,zb=ga,gb,sa,sb,ba,bb
mode = 0
if GSB==3:
    mode = 1
elif GSB==2:
    mode = 1
    if G==0:
        None
    elif S==0:
        xa,xb,ya,yb = sa,sb,ga,gb
    elif B==0:
        xa,xy,za,zb = ba,bb,ga,gb
elif GSB==1:
    mode = 0
    if G==1:
        None
    elif S==1:
        xa,xb,ya,yb = sa,sb,ga,gb
    elif B==1:
        xa,xy,za,zb = ba,bb,ga,gb
elif GSB==0:
    mode = 0

ans = 0
if GSB==0 or GSB==3:
    xa,xb,ya,yb,za,zb=min(xa,xb),max(xa,xb),min(ya,yb),max(ya,yb),min(za,zb),max(za,zb)
    if za > ya:
        ya,yb,za,zb = za,zb,ya,yb
    for x in range(N//xa+1):
        n0 = N - x*xa
        for y in range(n0//ya+1):
            n1 = n0 - y*ya
            z = n1//za
            n1 = n1 - z*za
            ans = max(ans,n1+x*xb+y*yb+z*zb)
elif GSB==1:
    if za > ya:
        ya,yb,za,zb = za,zb,ya,yb
    for y in range(N//ya+1):
        n = N - y*ya
        z = n//za
        n = n - z*za
        n = n + y*yb + z*zb
        x = n//xb
        n = n - x*xb
        ans = max(ans,n+x*xa)
elif GSB==2:
    if zb > yb:
        ya,yb,za,zb = za,zb,ya,yb
    for x in range(N//xa+1):
        n0 = N - x*xa + x*xb
        for y in range(n0//yb+1):
            n1 = n0 - y*yb
            z = n1//zb
            n1 = n1 - z*zb
            ans = max(ans,n1+y*ya+z*za)

print(ans)


