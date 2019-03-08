ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

H,W=rl()
a = [rl() for y in range(H)]

ans = []
cnt = 0
for y in range(1,H+1):
    odd = 0
    for x in range(1,W):
        if a[y-1][x-1]%2: odd ^= 1
        if odd == 1:
            cnt += 1
            ans.append([y,x,y,x+1])
    if odd==1:
        a[y-1][W-1] += 1

odd = 0
for y in range(1,H):
    if a[y-1][W-1]%2: odd ^= 1
    if odd == 1:
        cnt += 1
        ans.append([y,W,y+1,W])

print(cnt)
for i in range(cnt):
    print(*ans[i], sep=' ')