ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s = ri()

used = set()
ans = 1
while True:
    if s in used:
        break
    used.add(s)
    ans += 1
    s = f(s)
print(ans)