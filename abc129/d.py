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


H,W=rl()
S=[]
for i in range(H):
    S.append(input())
#M = [[0 for w in range(W)] for h in range(H)]
wM = [[0 for w in range(W)] for h in range(H)]
hM = [[0 for w in range(W)] for h in range(H)]

for h in range(H):
    cnt = 0
    for w in range(W):
        if S[h][w] == '#':
            #M[h][w] = 1
            wM[h][w-1] = cnt
            cnt = 0
        else:
            wM[h][w] = -1
            cnt += 1
    if cnt != 0:
        wM[h][W-1] = cnt

for h in range(H):
    cnt = 0
    for w in range(W-1,-1,-1):
        if wM[h][w] > 0:
            cnt = wM[h][w]
        elif wM[h][w] == -1:
            wM[h][w] = cnt

for w in range(W):
    cnt = 0
    for h in range(H):
        if S[h][w] == "#":
        #if M[h][w] == 1:
            hM[h-1][w] = cnt 
            cnt = 0
        else:
            hM[h][w] = -1
            cnt += 1
    if cnt != 0:
        hM[H-1][w] = cnt

for w in range(W):
    cnt = 0
    for h in range(H-1,-1,-1):
        if hM[h][w] > 0:
            cnt = hM[h][w]
        elif hM[h][w] == -1:
            hM[h][w] = cnt

ans = 0
for h in range(H):
    for w in range(W):
        ret1 = wM[h][w]
        ret2 = hM[h][w]
        ret = ret1 + ret2
        if ret1 != 0 and ret2 != 0:
            ret -= 1
        ans = max(ans,ret)
print(ans)