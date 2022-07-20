import sys
read = sys.stdin.readline
N = [i for i in read()]
N.pop()

if not str(0) in N:
    print(-1)
else :
    summation = 0
    for j in N :
        summation += int(j)
    if summation % 3 == 0 :
        N.sort(reverse=True)
        print(''.join(N))
    else :
        print(-1)