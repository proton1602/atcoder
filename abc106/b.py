ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
ans = 0
for n in range(1,N+1,2):
    res = 0
    for i in range(1,n+1):
        if n%i==0:
            res += 1
    if res == 8:
        ans += 1

print(ans)