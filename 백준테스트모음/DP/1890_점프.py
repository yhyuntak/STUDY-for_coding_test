import sys
read = sys.stdin.readline

N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int,read().split())))

# 우, 하
dr = [1,0]
dc = [0,1]

"""
그래프를 전부 탐색하면서 우,하에 갈 수 있는 곳에 +1을 해주면 된다.
"""
dp_table = [[0 for _ in range(N)] for _ in range(N)]
dp_table[0][0] = 1
for c in range(N):
    for r in range(N):
        if c == N-1 and r == N-1 :
            continue
        now = graph[c][r]
        for i in range(2):
            nr = r + dr[i] * now
            nc = c + dc[i] * now

            if 0<= nr < N and 0 <= nc < N and dp_table[c][r] != 0:
                dp_table[nc][nr] += dp_table[c][r]
# for j in range(N):
#     print(dp_table[j])
print(dp_table[-1][-1])
#
# # 갈 수 있는 곳이 있으면 dfs로 탐색하고
# # 갈 수 없는 곳에 도달하면 return 0
# # 도달 했다면 return 1
#
# def dfs(r,c):
#     # 먼저 현재 위치가 벽을 넘었는지부터 보자
#     if r<0 or r>=N or c<0 or c>=N :
#         return 0
#
#     # 현재 위치가 벽을 넘지 않았으면 여기부터 실행
#     # 종착점에 했으면 return 1하고 dfs끝
#     if graph[c][r] == 0 :
#         return 1
#     else :
#         # 그렇지 않다면 아래,오른쪽을 dfs로 탐색할 것.
#         temp = 0
#         for i in range(2):
#             nr = r+dr[i]*graph[c][r]
#             nc = c+dc[i]*graph[c][r]
#             temp += dfs(nr,nc)
#         return temp
# print(dfs(0,0))
