ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))
rr = lambda N: [ri() for _ in range(N)]
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')
OE = lambda x: print('Odd') if x%2 else print('Even')
INF = 10**18

s=input()

w_flag = -1
for i in range(len(s)):
    if w_flag == -1 and s[i] == "W":
        w_flag = i
        continue
    if w_flag != -1 and s[i] == "A":
        s = s[:w_flag] + "A" + "C"*(i-w_flag) + s[i+1:]
        w_flag = -1
    elif w_flag != -1 and s[i] != "A" and s[i] != "W":
        w_flag = -1

print(s)