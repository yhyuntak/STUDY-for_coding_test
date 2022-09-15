# 220915


import sys
read = sys.stdin.readline
N = int(read())
have_cards = list(map(int,read().split()))
have_cards.sort()
M = int(read())
have_numbers = list(map(int,read().split()))


def binary_search(start,end,number):

    while start <= end :

        mid = (start+end)//2
        mid_val = have_cards[mid]


        if mid_val == number :
            return True

        if mid_val > number :
            end = mid - 1
        else :
            start = mid + 1
    return False

for number in have_numbers :

    if binary_search(0,N-1,number):
        print(1,end=' ')
    else :
        print(0,end=' ')





# 220801
# import sys
# read = sys.stdin.readline
#
#
# def binary(N_list, start_idx, end_idx, M):
#
#     while start_idx <= end_idx:
#
#         mid_idx = (start_idx + end_idx) // 2
#         if N_list[mid_idx] == M:
#             return 1
#         elif N_list[mid_idx] < M:  # mid를 오른쪽으로 -> start_idx = mid_idx+1
#             start_idx = mid_idx + 1
#         elif N_list[mid_idx] > M:  # mid를 왼쪽으로 -> end_idx = mid_idx -1
#             end_idx = mid_idx - 1
#
#             # 만약 찾지 못하고 그냥 끝나버리면 -1 return
#     return 0
#
# N = int(read())
# N_list = list(map(int,read().split()))
# M = int(read())
# M_list = list(map(int,read().split()))
#
# # M에 대해 N_list를 훑으면 최대 500000*500000의 연산이 발생해 하나씩 훑는건 불가능
# # 따라서 빠르게 탐색하는 방법을 찾아야한다. -> 이분 탐색
# N_list.sort()
#
# start_idx = 0
# end_idx = len(N_list)-1
#
# for m in M_list :
#     print(binary(N_list,start_idx,end_idx,m), end=' ')
#
