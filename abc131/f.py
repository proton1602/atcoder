import sys
input = sys.stdin.readline
ri = lambda: int(input())
#rl = lambda: [int(x) if x.isdecimal() else x for x in input().split()]
#rl = lambda: list(input().split()))
rl = lambda: map(int,input().split())
rr = lambda N: [list(l) for l in zip(*[rl() for _ in range(N)])]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

N = ri()
X = [set() for i in range(10**5+1)]
Y = [set() for i in range(10**5+1)]
X_set = set()
Y_set = set()
for i in range(N):
    x,y=rl()
    X[x].add(y)
    Y[y].add(x)
    X_set.add(x)
    Y_set.add(y)

from collections import deque
sX = deque([-1])
sX.extend(list(X_set))
sY = deque([-1])
sY.extend(list(Y_set))
ans = 0


while True:
    sx = sX.pop()
    #print(sx,sX,cnt)
    if sx == -1:
        sX.appendleft(-1)
        break
    if len(X[sx]) >= 2:
        sx_Y = set()
        sx_Y_in = set()
        for y in X[sx]:
            sx_Y = sx_Y | Y[y]
        sx_Y_in = sx_Y_in | sx_Y 
        for y in X[sx]:
            sx_Y_in = sx_Y_in & Y[y]
            Y_dif = sx_Y - Y[y]
            for ssx in Y_dif:
                ans += 1
                X[ssx].add(y)
                Y[y].add(ssx)
        #print(ans,X[sx],sx_Y,sx_Y_in)
        if len(sx_Y - sx_Y_in) > 0:
            sX.extend(sx_Y - sx_Y_in)

while True:
    sy = sY.pop()
    #print(sy,sY,cnt)
    if sy == -1:
        sY.appendleft(-1)
        break
    if len(Y[sy]) >= 2:
        sy_X = set()
        sy_X_in = set()
        for x in Y[sy]:
            sy_X = sy_X | X[x]
        sy_X_in = sy_X_in | sy_X 
        for x in Y[sy]:
            sy_X_in = sy_X_in & X[x]
            X_dif = sy_X - X[x]
            for ssy in X_dif:
                ans += 1
                Y[ssy].add(x)
                X[x].add(ssy)
        #print(ans,Y[sy],sy_X,sy_X_in)
        if len(sy_X - sy_X_in) > 0:
            sY.extend(sy_X - sy_X_in)
while True:
    sx = sX.pop()
    #print(sx,sX,cnt)
    if sx == -1:
        sX.appendleft(-1)
        break
    if len(X[sx]) >= 2:
        sx_Y = set()
        sx_Y_in = set()
        for y in X[sx]:
            sx_Y = sx_Y | Y[y]
        sx_Y_in = sx_Y_in | sx_Y 
        for y in X[sx]:
            sx_Y_in = sx_Y_in & Y[y]
            Y_dif = sx_Y - Y[y]
            for ssx in Y_dif:
                ans += 1
                X[ssx].add(y)
                Y[y].add(ssx)
        #print(ans,X[sx],sx_Y,sx_Y_in)
        if len(sx_Y - sx_Y_in) > 0:
            sX.extend(sx_Y - sx_Y_in)

while True:
    sy = sY.pop()
    #print(sy,sY,cnt)
    if sy == -1:
        sY.appendleft(-1)
        break
    if len(Y[sy]) >= 2:
        sy_X = set()
        sy_X_in = set()
        for x in Y[sy]:
            sy_X = sy_X | X[x]
        sy_X_in = sy_X_in | sy_X 
        for x in Y[sy]:
            sy_X_in = sy_X_in & X[x]
            X_dif = sy_X - X[x]
            for ssy in X_dif:
                ans += 1
                Y[ssy].add(x)
                X[x].add(ssy)
        #print(ans,Y[sy],sy_X,sy_X_in)
        if len(sy_X - sy_X_in) > 0:
            sY.extend(sy_X - sy_X_in)
while True:
    sx = sX.pop()
    #print(sx,sX,cnt)
    if sx == -1:
        sX.appendleft(-1)
        break
    if len(X[sx]) >= 2:
        sx_Y = set()
        sx_Y_in = set()
        for y in X[sx]:
            sx_Y = sx_Y | Y[y]
        sx_Y_in = sx_Y_in | sx_Y 
        for y in X[sx]:
            sx_Y_in = sx_Y_in & Y[y]
            Y_dif = sx_Y - Y[y]
            for ssx in Y_dif:
                ans += 1
                X[ssx].add(y)
                Y[y].add(ssx)
        #print(ans,X[sx],sx_Y,sx_Y_in)
        if len(sx_Y - sx_Y_in) > 0:
            sX.extend(sx_Y - sx_Y_in)

while True:
    sy = sY.pop()
    #print(sy,sY,cnt)
    if sy == -1:
        sY.appendleft(-1)
        break
    if len(Y[sy]) >= 2:
        sy_X = set()
        sy_X_in = set()
        for x in Y[sy]:
            sy_X = sy_X | X[x]
        sy_X_in = sy_X_in | sy_X 
        for x in Y[sy]:
            sy_X_in = sy_X_in & X[x]
            X_dif = sy_X - X[x]
            for ssy in X_dif:
                ans += 1
                Y[ssy].add(x)
                X[x].add(ssy)
        #print(ans,Y[sy],sy_X,sy_X_in)
        if len(sy_X - sy_X_in) > 0:
            sY.extend(sy_X - sy_X_in)
print(ans)
