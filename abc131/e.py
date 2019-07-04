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

if (N-1)*(N-2)//2 < K:
    print(-1)
else:
    ans = []
    for v in range(2,N+1):
        ans.append((1,v))
    for i in range(2,N):
        if K >= (N-i):
            K -= (N-i)
        elif K == 0:
            for v in range(i+1,N+1):
                ans.append((i,v))
        else:
            for v in range(i+1,N+1-K):
                ans.append((i,v))
            K = 0
    print(len(ans))
    for u,v in ans:
        print(u,v)
