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

n=ri()
p=list(rl())
ans = 0
for i in range(1,n-1):
    p1,p2,p3 = p[i-1],p[i],p[i+1]
    p123 = [p1,p2,p3]
    if p2 != max(p123) and p2 != min(p123):
        ans += 1

print(ans)