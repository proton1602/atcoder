ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,Q=rl()
S=input()
sp = [[] for _ in range(26)]
A_o = ord('A')
for i in range(1,Q+1):
    t,d = input().split()
    sp[ord(t)-A_o].append([i,d])

CD = [[] for _ in range(N+2)]
direc = {'R':1, 'L':-1}
for i in range(1,N+1):
    for l,d in sp[ord(S[i-1])-A_o]:
        CD[i].append([l,0,i+direc[d]])
        CD[i+direc[d]].append([l,1,i])
for i in range(N+2):
    CD[i].sort()

C = [[0] for _ in range(N+2)]
D = [[0] for _ in range(N+2)]
for x in range(N+2):
    for y,io,fr in CD[x]:
        C[x].append(y)
        D[x].append([io,fr])

import bisect
def search_root(x,y):
    ind = bisect.bisect_left(C[x],y) - 1
    if ind==0:
        if x==0 or x==N+1:
            return 0
        else:
            return 1
    io, fr = D[x][ind]
    if io == 0:
        return 0
    else:
        if C[x][ind]==C[x][ind-1]:
            return search_root(fr,C[x][ind])
        else:
            return search_root(x,C[x][ind]) + search_root(fr,C[x][ind])

ans = N - (search_root(0,Q+1) + search_root(N+1,Q+1))
print(ans)
