import sys
read = sys.stdin.readline

# N은 서치 대상, M은 target 제공
N = int(read())
N_list = list(map(int,read().split()))
M = int(read())
M_list = list(map(int,read().split()))

plut_list = [0]*10000001
minus_list = [0]*10000001
for n in N_list :
    if n >= 0 :
        plut_list[n] += 1
    else :
        minus_list[-1*n] += 1

for m in M_list :
    if m >= 0 :
        print(plut_list[m],end=' ')
    else :
        print(minus_list[-1*m],end=' ')



#
# N_list.sort()
#
# # N,M이 음수도 있으니까 나는 이것을 둘로 가르겠다.
# minus_N_list = []
# plus_N_list = []
# for n in N_list :
#     if n >= 0 : plus_N_list.append(n)
#     else : minus_N_list.append(-1*n)
#
#
# def binary_search(graph,start,end,target,cnt):
#
#     if start >= end :
#         # 수를 찾아도 없으면 False 반환해서 넘어가는 것을 유도
#         print(cnt)
#         return cnt
#     mid = (start+end) // 2
#     if target == graph[mid] :
#         graph.pop(mid)
#         cnt += 1
#         return binary_search(graph,start,len(graph),target,cnt)
#     elif target < graph[mid] :
#         return binary_search(graph,start,mid-1,target,cnt)
#     else :
#         return binary_search(graph,mid+1,end,target,cnt)
#
# # result의 갯수를 세야하므로, 각각의 array를 구성.
# minus_result_array = []
# plus_result_array = []
#
# result_array = []
#
# from collections import deque
# M_list_q = deque(M_list)
# while M_list_q : # while문은 M_list가 사라질때까지 진행
#
#     target = M_list_q[0] # 항상 M_list의 첫번째가 target으로
#     cnt = 0 # 항상 cnt 갱신
#
#     # 만약 target이 양수 혹은 0이면
#     if target >= 0 :
#         # binary search를 해서 해당 값이 존재할때까지 갯수를 탐색
#         cnt = binary_search(plus_N_list,0,len(plus_N_list),target,cnt)
#         result_array.append(cnt)
#     # target이 음수면
#     else :
#         cnt = binary_search(minus_N_list,0,len(minus_N_list),-1*target,cnt)
#         result_array.append(cnt)
#
#     M_list_q.popleft()
#     print(M_list_q,target,result_array,cnt)
#     print(plus_N_list)
#     print(minus_N_list)