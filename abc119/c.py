ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,A,B,C=rl()
l=[0]*N
for i in range(N):
    l[i] = ri()
ans = float('inf')
for n in range(4**N):
    a,b,c=0,0,0
    ans_ = 0
    for i in range(N):
        sn = format(n>>(2*i),'0{}b'.format(N))[-2:]
        if sn=='01':
            a+=l[i]
            ans_ += 10
        elif sn=='10':
            b+=l[i]
            ans_ += 10
        elif sn=='11':
            c+=l[i]
            ans_ += 10
    if a!=0 and b!=0 and c!=0:
        ans_ += abs(A-a)+abs(B-b)+abs(C-c) -30
        if ans > ans_:
            ans = ans_

print(ans)