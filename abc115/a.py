ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

D=ri()
print('Christmas',end='')
for i in range(25-D):
    print(' Eve',end='')
print()