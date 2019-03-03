ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
INF = 10**18

N=ri()
xyh=[]
for i in range(N):
    xyh += [rl()]
xyh.sort(reverse=True, key=lambda x:x[2])

ans=[-1]*3
for x in range(101):
    if ans[0] != -1:
        break
    for y in range(101):
        if ans[0] != -1:
            break
        if xyh[0][2] == 0:
            h_m = xyh[0][2]+abs(x-xyh[0][0])+abs(y-xyh[0][1])
            for i in range(1,N):
                rst = xyh[i][2]+abs(x-xyh[i][0])+abs(y-xyh[i][1])
                if h_m > rst:
                    h_m = rst
                if h_m == 0:
                    break
                elif i==N-1:
                    ans = [x,y,h_m]
        else:
            h = xyh[0][2]+abs(x-xyh[0][0])+abs(y-xyh[0][1])
            for i in range(1,N):
                if xyh[i][2] != 0:
                    if h != xyh[i][2]+abs(x-xyh[i][0])+abs(y-xyh[i][1]):
                        break
                elif xyh[i][2] == 0:
                    if h > xyh[i][2]+abs(x-xyh[i][0])+abs(y-xyh[i][1]):
                        break
                if i == N-1:
                    ans = [x,y,h]

print("{} {} {}".format(ans[0],ans[1],ans[2]))