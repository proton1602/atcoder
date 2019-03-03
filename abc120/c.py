ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

S=input()
N=len(S)

buf = []
h = 0
ans = 0
for s in S:
    if s=='0':
        h -= 1
    else:
        h += 1
ans = N-abs(h)

print(ans)
