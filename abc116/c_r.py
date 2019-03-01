ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N = ri()
h = rl()

ans = 0
pre = 0
for i in h:
    if pre < i:
        ans += i - pre
    pre = i

print(ans)