import sys
read= sys.stdin.readline
N,M = map(int,read().split())
if N >= M :
    array_A = list(map(int,read().split()))
    array_B = list(map(int,read().split()))
else :
    array_B = list(map(int,read().split()))
    array_A = list(map(int,read().split()))

for b in array_B :
    start_idx = 0
    end_idx = len(array_A)-1
    while start_idx<=end_idx :
        if b < array_A[start_idx] :
            array_A = [b] + array_A
            break
            # print(b,results)
        if b > array_A[end_idx] :
            array_A = array_A[:end_idx+1] + [b] + array_A[end_idx+1:]
            break
        start_idx += 1
        end_idx -= 1

print(array_A)
