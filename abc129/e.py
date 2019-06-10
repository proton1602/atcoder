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

L = input().rstrip('\n')
N = len(L)

dp = [[0 for smaller in range(2)] for k in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    if L[i-1] == '1':
        dp[i][0] = dp[i-1][0]*2 % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][1] *3) % MOD
    elif L[i-1] == '0':
        dp[i][0] = dp[i-1][0] % MOD
        dp[i][1] = dp[i-1][1]*3 % MOD

print((dp[N][0]+dp[N][1])%MOD)


