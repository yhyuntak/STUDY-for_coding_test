# 다시풀어보자 다음에


























# import sys
# read = sys.stdin.readline
# from collections import deque
# N = int(read())
# M = int(read())
# # array = deque(list(map(int,read().split())))
# array = sorted(list(map(int,read().split())))
# 
# start_idx = 0
# end_idx = N-1
# 
# count = 0
# 
# while start_idx < end_idx :
#     left = array[start_idx]
#     right = array[end_idx]
#     print(left,right)
#     # 둘이 더했을 때 M이면 left-> <-right 하기
#     if left + right == M :
#         count += 1
#         start_idx +=1
#         end_idx -= 1
# 
#     # 둘이 더했을 때 값이 크면 right를 줄이기
#     elif left + right < M :
#         start_idx += 1
# 
#     # 둘이 더했을 때 값이 작으면 left를 키우기
#     else :
#         end_idx -=1
# 
# print(count)