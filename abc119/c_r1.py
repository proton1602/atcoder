ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,A,B,C=rl()
l=[ri() for _ in range(N)]
ans = 10**18
import itertools
for seq in itertools.product(range(4),repeat=N):
    a,b,c=0,0,0
    rst = 0
    for i in range(N):
        if seq[i]==1:
            a+=l[i]
            rst+=10
        elif seq[i]==2:
            b+=l[i]
            rst+=10
        elif seq[i]==3:
            c+=l[i]
            rst+=10
    if a*b*c != 0:
        rst += abs(A-a)+abs(B-b)+abs(C-c)-30
        if ans > rst:
            ans = rst

print(ans)