bingo_check = [[0 for _ in range(5)] for _ in range(5)]
bingo_graph = []
bingo_data = {}

for r in range(5):
    temp = list(map(int,input().split()))
    for j in range(5):
        bingo_data[temp[j]] = [r,j]

say_number = []
for _ in range(5):
    temp = list(map(int,input().split()))
    say_number += temp
def count_func():
    count = 0
    # 가로 확인
    for row in range(5):
        if sum(bingo_check[row]) == 5 :
            count+=1
    # 세로 확인
    for col in range(5):
        if bingo_check[0][col] +bingo_check[1][col] +bingo_check[2][col] +bingo_check[3][col] +bingo_check[4][col] == 5:
            count+=1
    # 대각선 확인
    if bingo_check[0][0] + bingo_check[1][1] + bingo_check[2][2] + bingo_check[3][3] + bingo_check[4][4] == 5:
        count += 1
    if bingo_check[0][-1] + bingo_check[1][-2] + bingo_check[2][-3] + bingo_check[3][-4] + bingo_check[4][-5] == 5:
        count += 1
    # print(count)
    return count

for idx,num in enumerate(say_number):
    loc = bingo_data[num]
    bingo_check[loc[0]][loc[1]] = 1
    # print(count_func())
    # print("{}번째".format(idx+1))
    if count_func() >= 3 :
        print(idx+1)
        break
# print(idx+1)