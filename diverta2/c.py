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
A=list(rl())
A.sort()
ans = []
a_min = A[0]
a_max = A[-1]
if a_max <= 0:
    for i in range(1,N-1):
        y = A[i]
        ans.append([a_max,y])
        a_max -= y
    ans.append([a_max,a_min])
elif a_min > 0:
    for i in range(1,N-1):
        y = A[i]
        ans.append([a_min,y])
        a_min -= y
    ans.append([a_max,a_min])
else:
    ind = 0
    for i in range(1,N):
        if A[i] > 0:
            ind = i
            break
    for i in range(1,ind):
        y = A[i]
        ans.append([a_max,y])
        a_max -= y
    for i in range(ind,N-1):
        y = A[i]
        ans.append([a_min,y])
        a_min -= y
    ans.append([a_max,a_min])


print(a_max-a_min)
for x,y in ans:
    print(x,y)
        