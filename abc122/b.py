ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

S=input()

ans = 0
res = 0
for s in S:
    if s in ['A','C','G','T']:
        res += 1
    else:
        ans = max(ans,res)
        res = 0
ans = max(ans,res)
print(ans)