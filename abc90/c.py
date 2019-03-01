ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

N,M=rl()

if N==1:
    if M==1:
        print(1)
    else:
        print(M-2)
else:
    if M==1:
        print(N-2)
    else:
        print((N-2)*(M-2))