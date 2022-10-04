N = int(input())
array = list(map(int,input().split()))

start_idx = 0
end_idx = len(array)-1

save_min_array = []
min_sums = 10e9
while start_idx < end_idx :

    sums = array[start_idx] + array[end_idx]
    if abs(0-min_sums) > abs(0-sums) :
        min_sums = sums
        save_min_array = [array[start_idx],array[end_idx]]

    # print(array[start_idx],array[end_idx],sums,save_min_array)


    if sums == 0 : # 그냥 이거 출력해버리기
        save_min_array = [array[start_idx],array[end_idx]]
        break
    elif sums > 0 :
        end_idx -= 1
    else :
        start_idx += 1

print(*save_min_array)