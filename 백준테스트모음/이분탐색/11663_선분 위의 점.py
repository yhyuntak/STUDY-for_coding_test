import sys
read = sys.stdin.readline

def find_start(s,e,p,v):
    while s<=e:
        m = (s + e) // 2
        if p[m] >= v :
            e = m-1
        else :
            s = m+1
    return s

def find_end(s, e, p, v):
    while s <= e:
        m = (s + e) // 2
        if p[m] > v:
            e = m - 1
        else:
            s = m + 1
    return e

N,M = map(int,read().split())
points = sorted(list(map(int,read().split())))

for _ in range(M):
    start,end = map(int,read().split())

    find_s = find_start(0, N - 1, points, start)
    find_e = find_end(0, N - 1, points, end)

    print(find_e+1 - find_s)