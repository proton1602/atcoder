import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD=10**9+7

N,M=rl()
A=rl()
B=[0]*M
C=[0]*M
for i in range(M):
    B[i],C[i]=rl()


D = []
for a in A:
    D.append([a,1])
for b,c in zip(B,C):
    D.append([c,b])

D.sort(reverse=True)

ans = 0
cnt = N
for val,num in D:
    if cnt >= num:
        cnt -= num
        ans += val*num
    else:
        ans += val*cnt
        break
print(ans)
