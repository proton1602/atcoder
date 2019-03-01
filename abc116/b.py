ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = ri()

t = [0 for _ in range(1000000)]

ans = 0
a = s
for i in range(1,1000000):
    if t[int(a)] == 1:
        ans = i
        break
    else:
        t[int(a)] = 1
    a = f(a)

print(ans)