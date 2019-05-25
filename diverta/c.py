ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N=ri()
S = [0]*N
ans = 0
a = 0
b = 0
ab = 0
for i in range(N):
    S[i] = input()
for i in range(N):
    s_ = S[i]
    ans += s_.count('AB')
    if s_[0]=='B': b+=1
    if s_[-1]=='A': a+=1
    if s_[0]=='B' and s_[-1]=='A': ab+=1

if ab == max(a,b) and ab != 0:
    ans += (ab-1)
else:
    ans += min(a,b)

print(ans)