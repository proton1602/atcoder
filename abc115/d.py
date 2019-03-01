ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,X=rl()

p = [0]*(N+1)
l = [0]*(N+1)
p[0]=1
l[0]=1

for i in range(1,N+1):
    p[i]=2*p[i-1]+1
    l[i]=2*l[i-1]+3


ans = 0

for i in range(N-1,-1,-1):
    if X==1:
        X -= 1
        break
    elif X <= 1+l[i]:
        X -= 1
        if i == 0:
            ans += 1
            break
    elif X == 1+l[i]+1:
        X -= 1+l[i]+1
        ans += p[i]+1
        break
    elif X <= 2+2*l[i]:
        X -= 2+l[i]
        ans += p[i]+1
        if i == 0:
            ans += 1
            break
    else:
        X -= 3+2*l[i]
        ans += 2*p[i]+1
        break
print(ans)