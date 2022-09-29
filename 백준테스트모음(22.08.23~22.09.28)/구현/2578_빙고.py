## 220914

graph_dict = {}
for rr in range(5):
    temp = list(map(int,input().split()))
    for cc,t in enumerate(temp) :
            graph_dict[t] = [rr,cc]

bingo_graph = [[0 for _ in range(5)] for _ in range(5)]

call_array = []
for r in range(5):
    temp = list(map(int,input().split()))
    call_array += temp

def row_bingo():
    counts = 0
    for r in range(5):
        if sum(bingo_graph[r]) == 5 :
            counts += 1
    return counts

def col_bingo():
    counts = 0
    for col in range(5):
        if bingo_graph[0][col] + bingo_graph[1][col] + bingo_graph[2][col] + bingo_graph[3][col] + bingo_graph[4][col] == 5:
            counts += 1
    return counts

def diag_bingo():
    r,c = 0,4
    first = 0
    for i in range(5):
        first += bingo_graph[r+i][c-i]
    r,c = 0,0
    second = 0
    for j in range(5):
        second += bingo_graph[r+j][c+j]
    return first//5 + second//5

for idx,val in enumerate(call_array):
    # print("--------{}--------".format(idx+1))
    gr,gc = graph_dict[val]
    bingo_graph[gr][gc] = 1
    # for xz in range(5):
    #     print(bingo_graph[xz])
    # print()
    # nr,nc,nd = row_bingo(),col_bingo(),diag_bingo()
    # print(nr,nc,nd)
    # print()
    num_of_lines = row_bingo() + col_bingo() + diag_bingo()
    if num_of_lines == 3 :
        break

print(idx+1)



# 220801
# bingo_check = [[0 for _ in range(5)] for _ in range(5)]
# bingo_graph = []
# bingo_data = {}
#
# for r in range(5):
#     temp = list(map(int,input().split()))
#     for j in range(5):
#         bingo_data[temp[j]] = [r,j]
#
# say_number = []
# for _ in range(5):
#     temp = list(map(int,input().split()))
#     say_number += temp
# def count_func():
#     count = 0
#     # 가로 확인
#     for row in range(5):
#         if sum(bingo_check[row]) == 5 :
#             count+=1
#     # 세로 확인
#     for col in range(5):
#         if bingo_check[0][col] +bingo_check[1][col] +bingo_check[2][col] +bingo_check[3][col] +bingo_check[4][col] == 5:
#             count+=1
#     # 대각선 확인
#     if bingo_check[0][0] + bingo_check[1][1] + bingo_check[2][2] + bingo_check[3][3] + bingo_check[4][4] == 5:
#         count += 1
#     if bingo_check[0][-1] + bingo_check[1][-2] + bingo_check[2][-3] + bingo_check[3][-4] + bingo_check[4][-5] == 5:
#         count += 1
#     # print(count)
#     return count
#
# for idx,num in enumerate(say_number):
#     loc = bingo_data[num]
#     bingo_check[loc[0]][loc[1]] = 1
#     # print(count_func())
#     # print("{}번째".format(idx+1))
#     if count_func() >= 3 :
#         print(idx+1)
#         break
# # print(idx+1)