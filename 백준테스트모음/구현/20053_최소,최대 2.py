import sys
read = sys.stdin.readline
T = int(read())

for t in range(T):

    N= int(read())
    temp = list(map(int,read().split()))
    print("{} {}".format(min(temp),max(temp)))

