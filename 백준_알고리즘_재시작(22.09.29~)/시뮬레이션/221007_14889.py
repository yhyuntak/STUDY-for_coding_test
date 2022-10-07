"""
두 능력치의 합을 최소로 만들자~
"""
import copy

N = int(input())
"""
사람이 한팀으로 묶이는걸 모두 탐색해야할듯

"""

# N명중 N/2를 중복 없이 출력해야함.
# 근데 그냥 comb랑 per같은걸 쓰면 양쪽 팀에 중복이 생겨서 효율적이지 않음.
# 그니까 dfs로 백트래킹을 하면서 A,B팀을 결정해주고 dfs가 끝남과 동시에 팀 점수들을 계산하자. (이때 permutation을 사용)

from itertools import permutations

point_map = []
for _ in range(N):
    point_map.append(list(map(int,input().split())))

"""
한팀에 1,2,3,4가 있으면 1,2 1,3 1,4 2,1 2,3 2,4 3,1 3,2 3,4 4,1 4,2 4,3을 다 계산해야함. -> permutation
"""

def calc_points(team):
    calc_val = 0
    for i,j in list(permutations(team,2)):

        calc_val += point_map[i-1][j-1]
    return calc_val

def dfs(number):

    if len(star_team) == int(N/2):
        global min_val

        min_val = min(abs(calc_points(star_team)-calc_points(link_team)),min_val)
        # print(number,star_team,link_team)

        return
    # for문으로 dfs를 돌려서 끝까지 가야됌.
    for j in range(number,min(int(N/2)+number,N)) :

        star_team.append(j)
        link_team.pop(link_team.index(j))
        dfs(j+1)
        star_team.pop()
        link_team.append(j)


# 1부터 N까지 N/2개만 star 팀에 들어갈 수 있음.

star_team = []
link_team = [i for i in range(1, N + 1)]
# 근데 1,2,3,4와 2,1,3,4는 같은 것이니까 중복처리를 하기 위해서 오름차순으로 할 것.
# 그렇게 되면 각 자리는 들어갈 수 있는 숫자의 제한이 생긴다.
# 예를 들면 첫째 자리는 1~N/2+1 둘째는 2~N/2+2 ... 마지막은 N/2 ~ N/2 + N/2  그니까, dfs의 for문을 start~N/2 + start로 하면 될듯?
# 이걸 생각해서 하면 시간을 굉장히 단축 가능.

min_val = 10e9
# 이 루프는 첫째 자리를 정해주는 루프임.
for start in range(1,int(N/2)+1): # 1부터 N/2까지 가능.
    # 첫째 자리를 넣었다가
    star_team.append(start)
    # 동시에 link_team의 숫자도 빼줘야함.
    link_team.pop(link_team.index(start))
    dfs(start+1) # dfs는 다음 루프에서 i+1번째를 표현하기 위해 start+1를 입력으로.
    # dfs 끝나면 빼서 다른 숫자를 준비하기.
    star_team.pop()
    # 링크 팀에 막 넣어줘도 되는게 숫자의 인덱스를 찾아서 pop할꺼기 때문에 상관 없음.
    link_team.append(start)

print(min_val)


# """
# 두 능력치의 합을 최소로 만들자~
# """
#
# N = int(input())
# """
# 사람이 한팀으로 묶이는걸 모두 탐색해야할듯
# """
#
# # N명중 N/2를 중복 없이 출력해야함.
#
# from itertools import combinations,permutations
#
# comb_list = list(combinations([i for i in range(1,N+1)],int(N/2)))
#
# point_map = []
# for _ in range(N):
#     point_map.append(list(map(int,input().split())))
#
# """
# 한팀에 1,2,3,4가 있으면 1,2 1,3 1,4 2,1 2,3 2,4 3,1 3,2 3,4 4,1 4,2 4,3을 다 계산해야함.
# """
#
# total_dict = { i:0 for i in range(1,N+1)}
#
# from copy import deepcopy
#
# min_val = 10e9
#
# for comb in comb_list :
#     temp_dict = deepcopy(total_dict)
#     star_team = 0
#     link_team = 0
#     for i,j in list(permutations(comb,2)) :
#         try:
#             del temp_dict[i]
#             del temp_dict[j]
#         except :
#             pass
#         star_team += point_map[i-1][j-1]
#
#     for m,n in list(permutations(list(temp_dict.keys()),2)) :
#         link_team += point_map[m-1][n-1]
#
#     min_val = min(min_val,abs(star_team-link_team))
# print(min_val)