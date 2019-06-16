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

N,M=rl()
S=list(rl())
T=list(rl())

S_set = set(S)
T_set = set(T)
ST_set = S_set & T_set
S_T = S_set - ST_set
T_S = T_set - ST_set
ST_list = list(ST_set)
ST_list.sort()
ST_dic_list = []
for i in range(len(ST_list)):
    ST_dic_list.append((ST_list[i],i))
ST_dic = dict(ST_dic_list)

X = []
Y = []
for s in S:
    if not s in S_T:
        X.append(ST_dic[s])
for t in T:
    if not t in T_S:
        Y.append(ST_dic[t])
N = len(X)
M = len(Y)
if N > M:
    N,M = M,N
    X,Y = Y,X

