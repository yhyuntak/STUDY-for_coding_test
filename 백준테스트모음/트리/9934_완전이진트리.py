# 220914
K = int(input())
array = list(map(int,input().split()))

# 깊이가 K인 트리를 만들자.
trees = [[] for _ in range(K)]


def dfs(temp_list,floor):
    if len(temp_list) == 0 :
        return
    mid = len(temp_list)//2
    trees[floor].append(temp_list[mid])
    dfs(temp_list[:mid], floor + 1)
    dfs(temp_list[mid+1:], floor + 1)

dfs(array,0)

for i in range(K):
    print(*trees[i]) # *는 벗기는 느낌이네.



"""
3
1 6 4 3 5 2 7
"""







# 220801
# K = int(input())
# array = list(map(int,input().split()))
# trees = [[] for _ in range(K)]
#
# # 변수는 global 선언을 해야하지만, 객체들을 그냥 적용되는 듯
#
# def dfs(array,x):
#     mid = len(array)//2
#     trees[x].append(array[mid])
#     if len(array) == 1:
#         return
#     dfs(array[:mid],x+1)
#     dfs(array[mid+1:],x+1)
#
# dfs(array,0)
# for i in range(K):
#     print(*trees[i])