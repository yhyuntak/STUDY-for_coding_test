import sys
read = sys.stdin.readline
from collections import deque

N = int(read())

time_array = []
for i in range(N):
    time_array.append(list(map(int,read().split())))

time_array.sort()

maximum_val = 0
for j in range(N):
    now_time = time_array[j]
    start_time = now_time[0]
    end_time = now_time[1]
    count = 1
    for k in range(j+1,N):
        compare_time = time_array[k]
        if compare_time[0] >= end_time :
            end_time = compare_time[1]
            count += 1
    if maximum_val < count :
        maximum_val = count
print(maximum_val)

# time_array = deque(time_array)
#
# start_time = time_array.popleft()
# start = start_time[0]
# min_time = abs(start_time[0]-start_time[1])
#
# # 같은 start 시간을 갖는 것들 중 가장 회의 시간이 짧은 것을 선택
# for i in range(N):
#     compare_time = time_array.popleft()
#     compare_min = abs(compare_time[0]-compare_time[1])
#     if min_time > compare_min :
#         min_time = compare_min
#
#     if compare_time[0] != start :
#         time_array.appendleft(compare_time)
#         break
#
#
