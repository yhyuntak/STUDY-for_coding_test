import sys
read = sys.stdin.readline
N = int(read())
array = list(map(int,read().split()))
array.sort()
budget = int(read())

start = 0
end = max(array)

while start <= end :

    mid = (start+end)//2
    s = 0
    for a in array:
        if a >= mid :
            s += mid
        else :
            s += a
    if s > budget :
        end = mid-1
    else :
        start = mid + 1

print(end)