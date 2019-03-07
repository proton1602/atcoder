ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

S=input()
T=input()

def n2l(s):
    seen = {}
    ret = []
    idx = 0
    for ch in s:
        if ch not in seen:
            seen[ch] = idx
            idx += 1
        ret.append(seen[ch])
    return ret

yn(n2l(S)==n2l(T))
    
