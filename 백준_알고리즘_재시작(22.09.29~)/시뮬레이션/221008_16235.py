from collections import deque
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())

soils = [[5 for _ in range(N)] for _ in range(N)] #양분 맵
trees = [[deque() for _ in range(N)] for _ in range(N)]
dead_trees = [[deque() for _ in range(N)] for _ in range(N)]

"""
봄 : 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가. 
하나의 칸에 여러 나무가 있으면 나이가 어린것부터 먹는다
양분이 부족해서 먹지 못하면 죽는다. 양분은 보존

여름 : 봄에 죽은게 양분으로 변함. 죽은 나무의 나이를 2로 나눈 몫이 양분으로 추가

가을 : 나부가 번식. 번식하는 나무는 나이가 5의 배수. 인접 8칸에 나이가 1인 나무가 생긴다. 

겨울 : 땅에 양분 추가. 

K년이 지났을 때, 살아있는 나무의 개수는?
"""
plus_soils = []
for _ in range(N):
    plus_soils.append(list(map(int,input().split())))

for _ in range(M):
    r,c,age = list(map(int,input().split()))
    trees[r-1][c-1].append(age)

# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

for year in range(K):

    # 1년엔 4개의 시즌이 있다.
    # 순서대로 봄 여름 가을 겨울을 구현하자.

    """
    spring
    """

    for r in range(N):
        for c in range(N):
            now_trees = trees[r][c]
            for k in range(len(now_trees)):
                tree_age = now_trees[k]
                if soils[r][c] >= tree_age :
                    # 양분 섭취
                    soils[r][c] -= tree_age
                    # 나무 성장
                    trees[r][c][k]+=1
                else :
                    """
                    여름
                    """
                    # 양분 흡수
                    for ll in range(k,len(now_trees)):
                        soils[r][c] += int(trees[r][c].pop()//2)
                    break
    # 나무가 있는 모든 곳을 봄,여름이 끝나면 가을이 온다.
    """
    가을
    """
    # 나무가 번식.
    # 나무의 나이가 5의배수이면, 주변에 나이가 1인 나무가 생긴다.
    # 근데 번식은 한번에 이뤄져야함. 그래서 순서대로 하면 문제가 발생할 수 있음.

    q = []#deque()
    # 그래서 q에 (살아있는 나무의 나이)%5==0인 살아남은 것들을 찾아서 추가해주자.
    for r in range(N):
        for c in range(N):
            now_trees = trees[r][c]
            for k in range(len(now_trees)):
                temp_tree = now_trees[k]
                if temp_tree % 5 == 0 :
                    for j in range(8):
                        nr,nc = r+dr[j],c+dc[j]
                        # 주변에 나무를 퍼트리자.
                        if 0<=nr<N and 0<=nc<N : # 단, 범위 내에서
                            trees[nr][nc].appendleft(1)
            """
            겨울
            """
            soils[r][c] += plus_soils[r][c]

num_trees = 0
for r in range(N):
    for c in range(N):
        num_trees += len(trees[r][c])
print(num_trees)