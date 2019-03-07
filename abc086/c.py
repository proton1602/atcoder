ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N = ri()
ans = 1
t,x,y=0,0,0
for i in range(N):
    t_,x_,y_=rl()
    if t_%2 != (x_+y_)%2:
        ans = 0
    if (t_ - t) < abs(x_-x)+abs(y_-y):
        ans = 0
    t,x,y=t_,x_,y_

if ans:
    print('Yes')
else:
    print('No')