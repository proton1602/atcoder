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

N,K=rl()
A=list(rl())
ans = 0
end = 0
en = 0
S = A[0]
for st in range(N):
    if S >= K:
        ans += N-en
        S -= A[st]
        continue
    for en in range(en+1,N):
        S += A[en]
        if S >= K:
            ans += N-en
            break
    S -= A[st]

print(ans)
