import sys
read = sys.stdin.readline

N = int(read())
array = list(map(int,input().split()))
array.sort()

best_samples = []

start_idx = 0
end_idx = N-1
min_val = 1e9

while start_idx < end_idx :

    start = array[start_idx]
    end = array[end_idx]

    sums = abs(start+end)
    if sums < min_val :
        # 저장하기
        best_samples = [start,end]
        min_val = sums
    if start+end >= 0 : # 양수가 좀 큰거니까 end를 땡기자
        end_idx -= 1
    else : # 음수가 큰거니까 start를 오른쪽으로
        start_idx += 1

    print(start,end,sums,min_val,best_samples)