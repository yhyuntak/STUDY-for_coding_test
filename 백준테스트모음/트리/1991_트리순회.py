import sys
read = sys.stdin.readline

N = int(read())

graph = {}
for i in range(1,N+1):
    root,left,right = read().split()
    graph[root] = [left,right]

def preorder(trees,now):
    print(now,end='')

    left = trees[now][0]
    right = trees[now][1]
    # left 순회
    if left != '.' :
        preorder(trees,left)
    # right 순회
    if right != '.' :
        preorder(trees,right)

# print의 순서만 바꿈으로써 이게 다 되네..;
# 아직은 잘 모르겠다.
def inorder(trees,now):

    left = trees[now][0]
    right = trees[now][1]
    # left 순회
    if left != '.' :
        inorder(trees,left)
    print(now,end='')
    # right 순회
    if right != '.' :
        inorder(trees,right)

def postorder(trees,now):

    left = trees[now][0]
    right = trees[now][1]
    # left 순회
    if left != '.' :
        postorder(trees,left)
    # right 순회
    if right != '.' :
        postorder(trees,right)
    print(now,end='')

preorder(graph, 'A')
print()
inorder(graph,'A')
print()
postorder(graph,'A')
