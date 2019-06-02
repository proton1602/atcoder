import sys
input = sys.stdin.readline
ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18
MOD=10**9+7

S = input()
len_S = len(S)

set_map = []
state = 0
st = 0
en = 0

for i in range(len_S):
    s = S[i]
    if state == 0:
        if s == 'A':
            state = 1
            st = i
    elif state == 1:
        if s == 'B':
            state = 2
        elif s == 'C':
            state = 0
    elif state == 2:
        if s == 'A':
            state = 1
            st = i
        elif s == 'B':
            state = 0
        elif s == 'C':
            state = 3
            en = i
    elif state == 3:
        if s == 'A':
            state = 5
        elif s == 'B':
            state = 4
        elif s == 'C':
            set_map.append([st,en])
            state = 0
    elif state == 4:
        if s == 'A':
            set_map.append([st,en])
            state = 1
            st = i
        elif s == 'B':
            set_map.append([st,en])
            state = 0
        elif s == 'C':
            state = 3
            en = i
    elif state == 5:
        if s == 'B':
            state = 6
        elif s == 'C':
            set_map.append([st,en])
            state = 0
    elif state == 6:
        if s == 'A':
            set_map.append([st,en])
            state = 1
            st = i
        elif s == 'B':
            set_map.append([st,en])
            state = 0
        elif s == 'C':
            state = 7
            en = i
    elif state == 7:
        if s == 'A':
            state = 5
        elif s == 'B':
            state = 8
        elif s == 'C':
            set_map.append([st,en])
            state = 0
    elif state == 8:
        if s == 'A':
            set_map.append([st,en])
            state = 1
            st = i
        elif s == 'B':
            set_map.append([st,en])
            state = 0
        elif s == 'C':
            state = 7
            en = i

if state >= 3:
    set_map.append([st,en])

ans = 0
for st,en in set_map:
    cnt = 0
    for i in range(st,en):
        if S[i] == 'A':
            cnt += 1
        elif S[i] == 'B':
            ans += cnt

print(ans)
