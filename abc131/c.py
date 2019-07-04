import sys
input = sys.stdin.readline
ri = lambda: int(input())
#rl = lambda: [int(x) if x.isdecimal() else x for x in input().split()]
#rl = lambda: list(input().split()))
rl = lambda: map(int,input().split())
rr = lambda N: [list(l) for l in zip(*[rl() for _ in range(N)])]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD = 10**9+7

A,B,C,D=rl()

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

CD = lcm(C,D)

ans = B - (A-1) - (B//C - (A-1)//C) - (B//D - (A-1)//D) + (B//CD - (A-1)//CD)

print(ans)
