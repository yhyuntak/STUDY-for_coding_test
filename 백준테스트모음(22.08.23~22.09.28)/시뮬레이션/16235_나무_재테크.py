import sys
read = sys.stdin.readline
from math import floor
from collections import deque

"""
어느정도 키우고 팔아서 수익을 얻기!
M개의 나무를 사서 땅에 심음. 한 칸에 여러개의 나무가 있을수도있다.

다음 과정을 반복

1. 봄 
1) 자신의 나이만큼 양분을 먹고 나이가 1 증가. 각각의 나무는 칸에 있는 양분만 먹을 수 있다.
2) 한 칸에 여러 개의 나무가 있으면, 나이가 어린 것부터 자기의 나이만큼 양분을 먹는다. 
3) 자기 나이만큼 양분이 없으면 그 나무는 바로 삭제

2. 여름
1) 봄에 죽은 나무가 양분으로 변한다. 죽은 나무마다 나이/2 만큼이 칸에 양분이 된다. 소수점 아래는 버린다

3. 가을
1) 나무가 번식하는데, 이 나무는 나이가 5의 배수여야한다. 인접한 8칸에 나이가 1인 나무 생성. NXN안에만 있어야

4. 겨울 로봇이 땅을 돌며 양분을 추가한다. 추가되는 양은 A[r][c]이고 입력으로 주어진다.

K년이 지난 후 살아있는 나무의 수는?

"""

N,M,K = map(int,read().split())
graph = [[5 for _ in range(N) ] for _ in range(N) ]

plus_array = []
for _ in range(N):
    # r번째줄 c번째는 A[r][c]를 표현한다.
    plus_array.append(list(map(int,read().split())))

trees = {}
for _ in range(M):
    # r,c,z가 주어지고, z는 나이이다.
    r,c,z = map(int,read().split())
    if trees.get((r,c)) is None :
        trees[r,c] = [z]
    else :
        trees[r,c].append(z)


# K년 이니까 for문을 사용하자

for k in range(K):

    # 먼저 봄부터 구현
    """        
    1. 봄 
    1) 자신의 나이만큼 양분을 먹고 나이가 1 증가. 각각의 나무는 칸에 있는 양분만 먹을 수 있다.
    2) 한 칸에 여러 개의 나무가 있으면, 나이가 어린 것부터 자기의 나이만큼 양분을 먹는다. 
    3) 자기 나이만큼 양분이 없으면 그 나무는 바로 삭제
    """
    # 나무 정보를 뽑지만 나이가 .. 음 이건 hash를 쓰는게 맞는거같은데? (deque사용하자)
    # key를 for문으로 뽑아서 사용
    print(trees)

