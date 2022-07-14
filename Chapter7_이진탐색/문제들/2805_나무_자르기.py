import sys
read =sys.stdin.readline

N,M = map(int,read().split())
trees = list(map(int,read().split()))

# 이진 탐색을 위해 정렬
trees.sort()

# M을 맞추기 위해 노력하자
start = 0
end = max(trees)

while (start<=end):
    H = (start+end)//2
    meters = 0

    for tree in trees:
        if tree - H > 0 :
            meters += ( tree - H)

    if meters >= M : # 너무 많이 잘랐으면, H를 좀더 키우자
        start = H+1

    else : # 너무 적게 잘랐으면 H를 줄이자.
        end = H-1

print(H)