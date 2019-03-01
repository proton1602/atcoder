ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N = ri()
h = rl()
hl = len(h)

ans = 0
flag = 0
for _ in range(sum(h)):
    if sum(h) == 0:
        break
    flag = 1
    for i in range(hl):
        if flag == 1 and h[i] != 0:
            flag = 0
            h[i] = h[i] - 1
            ans += 1
        elif flag == 0 and h[i] == 0:
            flag = 1
        elif flag == 0 and h[i] != 0:
            h[i] = h[i] - 1

print(ans)
