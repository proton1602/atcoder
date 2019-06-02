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

N,A,B,C,D=rl()
S=input()
M=[0]*(N+1)
for i in range(N):
    M[i] = 0 if S[i]=='.' else 1

ans = 1

flag_2 = 0
cnt = 0
for i in range(A-1,D):
    if M[i] == 1:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 2:
        flag_2 = 1
        break
if flag_2==1:
    ans = 0

flag_3 = 0
cnt = 0
if C > D:
    for i in range(B-2,D+1):
        if M[i] == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt>=3:
            flag_3 = 1
            break
    if flag_3 == 0:
        ans = 0

yn(ans)