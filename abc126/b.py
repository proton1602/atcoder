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

S=input().rstrip()
a=int(S[:2])
b=int(S[2:])
if 1<=a and a<=12 and 1<=b and b<=12:
    print('AMBIGUOUS')
elif 1<=b and b<=12:
    print('YYMM')
elif 1<=a and a<=12:
    print('MMYY')
else:
    print('NA')
