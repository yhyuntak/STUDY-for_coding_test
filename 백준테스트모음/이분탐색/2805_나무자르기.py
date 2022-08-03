import sys
read = sys.stdin.readline

N,M = map(int,read().split())
array = list(map(int,read().split()))

start = 0
end = max(array)

while start <= end :
    mid = (start+end)//2

    temp_sum = 0
    for a in array :
        if a - mid > 0 :
            temp_sum += a-mid

    if temp_sum >= M :
        start = mid +1
    else :
        end = mid -1

print(end)