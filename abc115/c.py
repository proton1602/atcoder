ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,K=rl()
h=[0]*N
for i in range(N):
    h[i] = ri()

h.sort()
s = h[K-1]-h[0]
ans = s

for i in range(1,N-(K-1)):
    s = h[i+K-1] - h[i]
    if ans > s:
        ans = s

print(ans)
