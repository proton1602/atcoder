ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N=ri()
X=[0]*N
Y=[0]*N
H=[0]*N
for i in range(N):
    X[i],Y[i],H[i]=rl()
xyh=list(zip(X,Y,H))
xyh.sort(reverse=True,key=lambda x:x[2])
X,Y,H = zip(*xyh)

ans=[-1]*3
for x in range(101):
    if ans[0] != -1:
        break
    for y in range(101):
        if ans[0] != -1:
            break
        rst = H[0]+abs(x-X[0])+abs(y-Y[0])
        for i in range(1,N):
            if H[i] != 0 and rst != H[i]+abs(x-X[i])+abs(y-Y[i]):
                break
            elif H[i] == 0 and rst > H[i]+abs(x-X[i])+abs(y-Y[i]):
                break
            if i == N-1:
                ans = [x,y,rst]

print("{} {} {}".format(ans[0],ans[1],ans[2]))