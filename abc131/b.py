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

N,L=rl()
azi = [L+i-1 for i in range(1,N+1)]
S = sum(azi)
ind = 0
M = INF
for i in range(N):
    a = azi[i]
    if abs(a) < M:
        M = abs(a)
        ind = i

print(S-azi[ind])