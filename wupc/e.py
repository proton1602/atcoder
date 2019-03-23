ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

M,N=rl()
r = [0]*M
c = [0]*N
for i in range(M):
    a = input()
    r[i] = a.count('1')
    for j in range(N):
        c[j] += int(a[j])

def mirror(l,i,j):
    i_max = (i+j-1)//2
    for dif in range(i_max-i+1):
        if l[i+dif] != l[j-dif]:
            return 0
    return 1
R = [0]*M
r0 = r[0]
r0l = 0
r0M = [r0]*M
if r != r0M:
    for i in range(M-1):
        if r[i] == r0:
            R[i] = 1
        else:
            r0l = i
            break
    for i in range(M-1,r0l-1,-1):
        if r[i] != r0:
            continue
        else:
            R[i] = mirror(r,1,i-1)
    for i in range(M-1):
        if R[i] == 0:
            continue
        else:
            R[i] = mirror(r,i+1,M-1)
    R = sum(R)
else:
    R = M-1



C = [0]*N
c0 = c[0]
c0l = 0
c0N = [c0]*N
if c != c0N and R != 0:
    for i in range(N-1):
        if c[i] == c0:
            C[i] = 1
        else:
            c0l = i
            break
    for i in range(N-1,c0l-1,-1):
        if c[i] != c0:
            continue
        else:
            C[i] = mirror(c,1,i-1)
    for i in range(N-1):
        if C[i] == 0:
            continue
        else:
            C[i] = mirror(c,i+1,N-1)
    C = sum(C)
else:
    C = N-1

print(R*C)