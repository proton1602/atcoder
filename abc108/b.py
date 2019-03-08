ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

a,b,c,d=rl()
v2_1 = [a-c,b-d]
v2_3 = [v2_1[1],-v2_1[0]]
x3 = c+v2_3[0]
y3 = d+v2_3[1]
x4 = x3+v2_1[0]
y4 = y3+v2_1[1]

print(x3,y3,x4,y4)