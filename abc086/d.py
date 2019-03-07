ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,K=rl()
X = [0]*N
Y = [0]*N
C = [0]*N
W = [[0 for _ in range(2*K+1)] for _ in range(2*K+1)]
B = [[0 for _ in range(2*K+1)] for _ in range(2*K+1)]
for i in range(N):
    x,y,c=input().split()
    x = int(x)%(2*K)
    y = int(y)%(2*K)
    X[i] = x
    Y[i] = y
    if c == 'W':
        W[x][y] += 1
        C[i] = 0
    else:
        B[x][y] += 1
        C[i] = 1

for xy in range(1,2*K):
    W[xy][0] += W[xy-1][0]
    W[0][xy] += W[0][xy-1]
    B[xy][0] += B[xy-1][0]
    B[0][xy] += B[0][xy-1]
for x in range(1,2*K):
    for y in range(1,2*K):
        W[x][y] += W[x-1][y] + W[x][y-1] - W[x-1][y-1]
        B[x][y] += B[x-1][y] + B[x][y-1] - B[x-1][y-1]

ans = 0
for x in range(K+1):
    for y in range(K+1):
        res = (W[x-1][y-1] +
        B[x+K-1][y-1] - B[x-1][y-1] +
        W[2*K-1][y-1] - W[x+K-1][y-1] + 
        B[x-1][y+K-1] - B[x-1][y-1] +
        W[x+K-1][y+K-1] - W[x-1][y+K-1] - W[x+K-1][y-1] + W[x-1][y-1] +
        B[2*K-1][y+K-1] - B[x+K-1][y+K-1] - B[2*K-1][y-1] + B[x+K-1][y-1] +
        W[x-1][2*K-1] - W[x-1][y+K-1] +
        B[x+K-1][2*K-1] - B[x-1][2*K-1] - B[x+K-1][y+K-1] + B[x-1][y+K-1] + 
        W[2*K-1][2*K-1] - W[x+K-1][2*K-1] - W[2*K-1][y+K-1] + W[x+K-1][y+K-1])

        ans = max(ans,res)

print(ans)

    