import sys
read = sys.stdin.readline

N = int(read())
graph = []
for _ in range(N):
    temp = list(map(int,read().split()))
    graph.append(temp)
tnd = [N//2,N//2]

# 좌 하 우 상 순으로
dr = [0,1,0,-1]
dc = [-1,0,1,0]

def mimon(row,col,d,val):
    global  results

    coord = [[dr[d] * 2,dc[d] * 2],[dr[(d+1)%4] * 2,dc[(d+1)%4] * 2],[dr[(d + 3) % 4] * 2,dc[(d + 3) % 4] * 2],\
             [dr[d] + dr[(d + 3) % 4],dc[d] + dc[(d + 3) % 4]],[dr[d] + dr[(d + 1) % 4],dc[d] + dc[(d + 1) % 4]],\
                 [dr[(d+1)%4],dc[(d+1)%4]],[ dr[(d + 3) % 4] ,dc[(d + 3) % 4] ], \
             [ dr[(d+2)%4] + dr[(d + 3) % 4] , dc[(d+2)%4] + dc[(d + 3) % 4] ], [  dr[(d+2)%4] + dr[(d + 1) % 4] , dc[(d+2)%4] + dc[(d + 1) % 4] ]]
    prod = [0.05,0.02,0.02,0.1,0.1,0.07,0.07,0.01,0.01]

    prop = 0
    for cc,p in zip(coord,prod):
        n_row ,n_col = row+cc[0],col+cc[1]
        sand = int(val*p)
        prop += sand
        if 0<= n_row < N and 0<= n_col < N :
            graph[n_row][n_col] += sand
        else :
            results += sand

    # 비율로 나눠주던게 다끝나면 a로 나머지를 주자.
    n_row,n_col = row+dr[d], col+ dc[d]

    if 0 <= n_row < N and 0 <= n_col < N:
        graph[n_row][n_col] += graph[row][col] - prop
    else:
        results += graph[row][col] - prop

    # graph[r + dr[d] * 2][c + dr[d] * 2] += val * 0.05
    # graph[r + dr[(d+1)%4] * 2][c + dr[(d+1)%4] * 2] += val * 0.02
    # graph[r + dr[(d + 3) % 4] * 2][c + dr[(d + 3) % 4] * 2] += val * 0.02

    # graph[r + dr[d] + dr[(d + 3) % 4]][c + dr[d] + dr[(d + 3) % 4]] += val * 0.1
    # graph[r + dr[d] + dr[(d + 1) % 4]][c + dr[d] + dr[(d + 1) % 4]] += val * 0.1

    # graph[r + dr[(d+1)%4] ][c + dr[(d+1)%4] ] += val * 0.07
    # graph[r + dr[(d + 3) % 4] ][c + dr[(d + 3) % 4]] += val * 0.07
    #
    # graph[r + dr[(d+2)%4] + dr[(d + 3) % 4]][c + dr[(d+2)%4] + dr[(d + 3) % 4]] += val * 0.01
    # graph[r + dr[(d+2)%4] + dr[(d + 1) % 4]][c + dr[(d+2)%4] + dr[(d + 1) % 4]] += val * 0.01
    #
    # graph[r + dr[d] ][c + dr[d]] += val * 0.55


r, c = tnd[0], tnd[1]
results = 0
for n in range(3,N+1,2):
    init = []
    for i in range(1,5):
        for j in range(n-1) :
            init.append(i%4)
    init[0] = 0
    for m in init :
        r,c = r+dr[m],c+dc[m]

        # 움직임 구현은 끝났고
        # 이제 먼지가 어떻게 되는지만 만들자.

        # 다음 위치. 그니까 내 코드에선 r,c를 중심으로 해야함.
        # print(n,r,c,m,init)
        mimon(r,c,m,graph[r][c])
        graph[r][c] = 0
        #
        # print(r,c,m,results)
        # for _ in range(N):
        #     print(graph[_])
        # print()

print(results)