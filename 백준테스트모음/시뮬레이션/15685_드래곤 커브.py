"""
드래곤 커브는 시작점 시작방향 세대로 구성

음 일단 아래방향이 +y 오른쪽방향이 +x 이다.

N 세대 커브는 N-1세대의 끝점을 기준으로 시계방향으로 90도 회전 시키는 느낌

문제는 사각형의 4개의 점이 모두 드래곤 커브의 일부인 사각형들의 개수를 구하는 것.
"""

N = int(input())



info_array = []
for _ in range(N):
    info_array.append(list(map(int,input().split())))

