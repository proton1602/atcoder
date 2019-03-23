ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

N,A,B=rl()
P=rl()

for i in range(N):
    P[i] -= (i+1)

ans = 0
while True:
    abs_max = -1
    ind = 0
    for i in range(N):
        a_p = abs(P[i])
        if abs_max < a_p:
            abs_max = a_p
            ind = i
    if abs_max == 0:
        break

    if P[ind] > 0:
        ans += min(B,A*P[ind])
        for i in range(ind+1,ind+P[ind]+1):
            P[i] += 1
        P[ind] = 0
    else:
        ans += min(A,B*(-P[ind]))
        for i in range(ind+P[ind],ind):
            P[i] -= 1
        P[ind] = 0


print(ans)
