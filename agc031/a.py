ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9 + 7

N=ri()
S=input()

cnt = [1]*26
ord_a = ord('a')

for s in S:
    cnt[ord(s) - ord_a] += 1

ans = 1
for c in cnt:
    ans *= c
    ans %= MOD

ans -= 1
print(ans)