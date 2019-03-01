ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,M=rl()
X=rl()
X.sort()
d = [X[i+1]-X[i] for i in range(M-1)]
d.sort()
to = M - N
print(sum(d[0:to]) if to>0 else 0)
