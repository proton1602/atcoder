N = int(input())
A = [int(i) for i in input().split()]

m = min(A)

def MBR(l):
    print(l)
    global m
    l1 = [i for i in l if i > 0]
    if l1:
        m1 = min(l1)
        if m > m1:
            m = m1
    [MBR([m % i for m in l if m > 0]) for i in l if i > 0]

MBR(A)
print(m)

