ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N,M=rl()
A=[0]*M
B=[0]*M
for i in range(M):
    A[i],B[i] = rl()

class UnionFind:
    def __init__(self,n):
        self.par = [-1 for i in range(n+1)]
    
    def find(self,x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def same_check(self,x,y):
        return self.find(x) == self.find(y)
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        w_x = -self.par[x]
        w_y = -self.par[y]
        if w_x > w_y:
            self.par[x] += self.par[y]
            self.par[y] = x
        else:
            self.par[y] += self.par[x]
            self.par[x] = y
        return w_x*w_y
        
ans = [0]*M
res = N*(N-1)//2
uf = UnionFind(N)
for i in range(M-1,-1,-1):
    ans[i] = res
    a,b = A[i],B[i]
    if not uf.same_check(a,b):
        res -= uf.union(a,b)

for i in range(M):
    print(ans[i])