# 가로 C, 세로 R임.
# 좌측상단이 1,1임
R,C = map(int,input().split())
graph = []
for _ in range(R):
    temp = input()
    graph.append([t for t in temp])


# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는
# 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 말이 최대로 움직일 수 있는 횟수는??
# 한번 갔던길은 다시 못돌아 오기 때문에 항상 maximum 값을 비교하면 더 효율적일듯.
maximum_result = 1

# 한번 갔던 알파벳에 다시 안가기 위한 26개의 list 생성

word_dict = [0 for _ in range(26)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 시작점
sr,sc = 0,0
word_dict[alphabet.index(graph[sr][sc])] = 1

# DFS로 풀어야 잘 풀리는 문제다.

def dfs(now_r,now_c,cnt):
    global maximum_result
    maximum_result = max(maximum_result, cnt)
    # dfs 시작
    for i in range(4):
        next_r,next_c = now_r+dr[i],now_c+dc[i]
        if 0<= next_r < R and 0<= next_c < C : # 안정적인 구간에서
            # 알파벳이 중복되는지 확인
            idx = alphabet.index(graph[next_r][next_c])
            if word_dict[idx] == 0 : # 중복되지 않으면 앞으로 가기.
                # print(next_r,next_c,cnt)
                # 한칸 더 갔으니 cnt 증가.
                cnt += 1
                # 물론 단어도 추가할 것
                word_dict[idx] += 1
                cnt = dfs(next_r,next_c,cnt)
    # 여기에 온다는 것은 더이상 갈 곳이 없다는 것을 의미한다.
    # 따라서 자기 자신 graph[now_r][now_c] 는 안 간 것처럼 만들어줘야해.
    word_dict[alphabet.index(graph[now_r][now_c])] = 0
    cnt -= 1

    return cnt

dfs(sr,sc,1)
print(maximum_result)



#
# # 지만 BFS로 풀면 충분하다.
#
# from collections import deque
#
# q = deque()
# q.append([sr,sc])
#
# while q :
#     now_r,now_c = q.popleft()
#
#     for i in range(4):
#         next_r,next_c = now_r+dr[i],now_c+dc[i]
#         if 0<= next_r < R and 0<= next_c < C and visited[next_r][next_c] == 0 : # 한번도 가보지 않은 안정적인 구간에서
#             # 알파벳이 중복되든 안되는 방문했다는 표현하기.
#             visited[next_r][next_c] = -1
#             # 알파벳이 중복되는지 확인
#             if word_dict.get(graph[next_r][next_c]) is None : # 중복되지 않으면 앞으로 가기.
#                 # 앞으로 가는 곳만 visited를 정상적으로 표현하기.
#                 visited[next_r][next_c] = visited[now_r][now_c] + 1
#                 q.append([next_r,next_c])
#                 # 그리고 항상 maximum값과 비교하기.
#                 maximum_result = max(maximum_result,visited[next_r][next_c])
#                 # 물론 단어도 추가할 것
#                 word_dict[graph[next_r][next_c]] = 1
#     for j in range(R):
#         print(visited[j])
#
#     print(maximum_result)
#
