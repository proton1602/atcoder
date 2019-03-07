ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

S=input()
T=input()

dT = dict()
dS = dict()

for i,t in enumerate(T):
    if t not in dT:
        dT[t] = [i]
    else:
        dT[t].append(i)
for i,s in enumerate(S):
    if s not in dS:
        dS[s] = [i]
    else:
        dS[s].append(i)

def ans():
    for c in map(chr,range(ord('a'),ord('z')+1)):
        if c in dT:
            res = S[dT[c][0]]
            for i in dT[c]:
                if res != S[i]:
                    return 0
    for c in map(chr,range(ord('a'),ord('z')+1)):
        if c in dS:
            res = T[dS[c][0]]
            for i in dS[c]:
                if res != T[i]:
                    return 0
    return 1

yn(ans())
    
