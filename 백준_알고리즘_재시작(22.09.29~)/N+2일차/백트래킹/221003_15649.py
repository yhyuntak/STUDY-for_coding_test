# 인터넷 풀이

N,M= map(int,input().split())
now_comb = [] # 조합을 저장해서 일정 길이가 되면 출력하고 return후 다시 초기화를 반복하네
def dfs():
    if len(now_comb) == M :
        print(*now_comb)
        return
    for i in range(1,N+1):
        if i not in now_comb :
            now_comb.append(i)
            dfs()
            now_comb.pop() # 와 이게 N,M=3,2로 해서 해보면 1이 1,2 / 1,3이 끝나면 pop으로 빠지고 2가 시작되네.. 미쳤다
dfs()





# 내 풀이
#
# """
# 1~N까지 중복없이 M개를 고른 수열을 모두 구하라
# """
# import copy
#
# N,M= map(int,input().split())
#
# def dfs(val,array):
#     if len(val) == M :
#         save_array.append(val)
#         return
#
#     for k in range(1,N+1):
#         if array[k-1] == 0 : # 이미 빠져있는 수라면 패스
#             continue
#         else :
#             temp = copy.deepcopy(array)
#             temp_val = copy.deepcopy(val)
#             temp_val.append(temp[k-1])
#             temp[k-1] = 0
#             dfs(temp_val,temp)
#
#
# num_array = [ i for i in range(1,N+1)] # [1,2,...N]
# save_array = []
# for j in range(1,N+1):
#     # 뭐든 시작이 될 수 있음.
#     temp_array = copy.deepcopy(num_array)
#     temp_val = [j]
#     temp_array[j-1] = 0
#     dfs(temp_val,temp_array)
#
# for comb in save_array :
#     print(*comb)
