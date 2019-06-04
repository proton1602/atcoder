import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

N,M=rl()
S = [[0]*(N+1) for _ in range(M)]
for i in range(M):
    k, *s = rl()
    for s_ in s:
        S[i][s_] = 1
P=rl()

ans = 0
import itertools
for switch in itertools.product(range(2),repeat=N):
    ret = 0
    for p, s in zip(P,S):
        cnt = 0
        for i in range(N):
            cnt += switch[i]*s[i+1]
        if p != cnt%2:
            break
        ret += 1
    ans += ret//M

print(ans)
