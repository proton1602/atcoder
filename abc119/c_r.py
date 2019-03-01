ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,A,B,C=rl()
l=[ri() for _ in range(N)]

def dfs(cur,a,b,c):
    if cur==N:
        return abs(A-a)+abs(B-b)+abs(C-c)-30
    ret0 = dfs(cur+1,a,b,c)
    ret1 = dfs(cur+1,a+l[cur],b,c)+10
    ret2 = dfs(cur+1,a,b+l[cur],c)+10
    ret3 = dfs(cur+1,a,b,c+l[cur])+10
    return min(ret0,ret1,ret2,ret3)

print(dfs(0,0,0,0))