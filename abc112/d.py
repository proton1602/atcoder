ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,M=rl()

if M%N==0:
    print(M//N)
else:
    x = M//N
    ans = 1
    for i in range(x,0,-1):
        if M%i != 0:
            continue
        else:
            ans = i
            break
    print(ans)

