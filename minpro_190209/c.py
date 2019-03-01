K,A,B = map(int, input().split())
C = B - A
if C > 2 and K > 1:
    K_rem = K - (A - 1)
    if K_rem > 1:
        print(A + C*(K_rem//2) + K_rem % 2)
    else:
        print(1+K)
else:
    print(1+K)

