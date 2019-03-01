ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

a,b = rl()

a -= 1
b -= 1

print("{} {}".format(100,100))
for i in range(100):
    s = ''
    for j in range(100):
        if j < 50:
            if j%2==0 and i%2==0 and j<49 and a>0:
                s += '.'
                a -= 1
            else:
                s += '#'
        else:
            if j%2==0 and i%2==0 and j>51 and b>0:
                s += '#'
                b -= 1
            else:
                s += '.'
    print(s)

