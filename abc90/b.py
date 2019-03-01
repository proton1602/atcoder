ri = lambda: int(input())
rl = lambda: list(map(int,input().split()))

A,B=rl()

c_a = A//100 - 100 + 1
c_b = B//100 - 100 + 1
if A > (A//100*100 + A//10000 + (A//1000-A//10000*10)*10):
    c_a += 1
if B >= (B//100*100 + B//10000 + (B//1000-B//10000*10)*10):
    c_b += 1

print(c_b-c_a)
