ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N=ri()
D,X=rl()
A=[0]*N
ans = X
for i in range(N):
    ans += (D-1)//ri() + 1

print(ans)