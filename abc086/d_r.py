ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,K=rl()

W = [[0 for _ in range(2*K+3)] for _ in range(2*K+3)]
for i in range(N):
    x,y,c=input().split()
    x = int(x)%(2*K)
    y = (int(y) if c=='W' else int(y)+K)%(2*K)
    if (x<K)^(y<K):
        x %= K
        y %= K
        W[0][y+1] += 1
        W[0][y+K+1] -= 1
        W[x+1][0] += 1
        W[x+1][y+1] -= 2
        W[x+1][y+K+1] += 2
        W[x+1][2*K] -= 1
        W[x+K+1][0] -= 1
        W[x+K+1][y+1] += 2
        W[x+K+1][y+K+1] -= 2
        W[x+K+1][2*K] += 1
        W[2*K][y+1] -= 1
        W[2*K][y+K+1] += 1
    else:
        x %= K
        y %= K
        W[0][0] += 1
        W[x+1][0] -= 1
        W[0][y+1] -= 1
        W[x+1][y+1] += 2
        W[x+K+1][y+1] -= 2
        W[x+1][y+K+1] -= 2
        W[x+K+1][y+K+1] += 1
        W[x+K+1][0] += 1
        W[2*K][0] -= 1
        W[2*K][y+1] += 1
        W[0][y+K+1] += 1
        W[0][2*K] -= 1
        W[x+1][2*K] += 1

ans = 0
for x in range(0,2*K+1):
    for y in range(0,2*K+1):
        W[x][y] += W[x][y-1]
for y in range(0,2*K+1):
    for x in range(0,2*K+1):
        W[x][y] += W[x-1][y]
        ans = max(ans,W[x][y])

print(ans)