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
AB = []
for i in range(N):
    a,b = rl()
    AB.append((a,b))

AB.sort(key = lambda x: x[1])

time = 0
res = 0
ans = 1
for a,b in AB:
    if time < b:
        res += (b-time)
        time = b
    if res >= a:
        res -= a
    else:
        ans = 0
        break

yn(ans)