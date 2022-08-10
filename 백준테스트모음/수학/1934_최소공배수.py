import sys
read = sys.stdin.readline

T= int(read())
for _ in range(T):
    a,b = map(int,read().split())
    aa, bb = a, b

    while a % b != 0:
        a, b = b, a % b

    print(aa * bb // b)