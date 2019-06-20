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

N=ri()
A=list(rl())
cnt = [0]*3
ans = 0
sei = []
for a in A:
    sei.append(abs(a))
    ans += abs(a)
    if a > 0:
        cnt[0] += 1
    elif a == 0:
        cnt[1] += 1
    elif a < 0:
        cnt[2] += 1

if cnt[1] > 0 or cnt[2]%2 == 0:
    None
else:
    ans -= 2 * min(sei)

print(ans)