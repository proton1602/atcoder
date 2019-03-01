ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N=ri()
ans = 0
rate = 380000.0
for i in range(N):
    x,u=input().split()
    x = float(x)
    ans += x if u=='JPY' else x*rate

print("{:11f}".format(ans))