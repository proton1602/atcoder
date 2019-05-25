ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

X,Y,Z,K=rl()
A=rl()
B=rl()
C=rl()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
ans = []
for a in range(1,X+1):
    for b in range(1,Y+1):
        for c in range(1,Z+1):
            if a*b*c<=K:
                ans.append(A[a-1]+B[b-1]+C[c-1])
            else:
                break
ans.sort(reverse=True)
for i in range(K):
    print(ans[i])