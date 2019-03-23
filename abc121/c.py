ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,M=rl()
AB = []
for i in range(N):
    a,b=rl()
    AB.append([a,b])

AB.sort()

ans = 0
for a,b in AB:
    if M == 0:
        break
    if M > b:
        ans += a*b
        M -= b
    else:
        ans += a*M
        M -= M

print(ans)