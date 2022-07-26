K = int(input())
array = list(map(int,input().split()))
trees = [[] for _ in range(K)]

# 변수는 global 선언을 해야하지만, 객체들을 그냥 적용되는 듯

def dfs(array,x):
    mid = len(array)//2
    trees[x].append(array[mid])
    if len(array) == 1:
        return
    dfs(array[:mid],x+1)
    dfs(array[mid+1:],x+1)

dfs(array,0)
for i in range(K):
    print(*trees[i])