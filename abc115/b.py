ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N=ri()
p=[0]*N
for i in range(N):
    p[i] = ri()

print(sum(p)-max(p)//2)