ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18
 
N,K=rl()
 
W = [[0 for _ in range(K+3)] for _ in range(K+3)]
for i in range(N):
    x,y,c=input().split()
    x = int(x)%(2*K)
    y = (int(y) if c=='W' else int(y)+K)%(2*K)
    if (x<K)^(y<K):
        x %= K
        y %= K
        W[0][y+1] += 1
        W[x+1][y+1] -= 2
        W[0][K+1] -= 1
        W[x+1][K+1] += 1
        W[x+1][0] += 1
        W[K+1][0] -= 1
        W[K+1][y+1] += 1
    else:
        x %= K
        y %= K
        W[0][0] += 1
        W[x+1][0] -= 1
        W[0][y+1] -= 1
        W[x+1][y+1] += 2
        W[K+1][y+1] -= 1
        W[x+1][K+1] -= 1
        W[K+1][K+1] += 1
 
for x in range(0,K+2):
    for y in range(0,K+2):
        W[x][y] += W[x][y-1]
for y in range(0,K+2):
    for x in range(0,K+2):
        W[x][y] += W[x-1][y]
 
ans = 0
for x in range(K+1):
    for y in range(K+1):
        res = W[x][y]
        ans = max(ans,res,N-res)
 
print(ans)