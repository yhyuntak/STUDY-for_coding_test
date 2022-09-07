# 220907
N = int(input())
trees = {}
for _ in range(N):
    a,b,c = input().split()
    trees[a] = [b,c]

start = 'A'
def preorder(start):
    if start == '.' :
        return

    # 부모의 자식은 2개씩 무조건.
    left = trees[start][0]
    right = trees[start][1]

    print(start,end='')
    preorder(left)
    preorder(right)

def inorder (start):
    if start == '.' :
        return

    # 부모의 자식은 2개씩 무조건.
    left = trees[start][0]
    right = trees[start][1]

    inorder(left)
    print(start,end='')
    inorder(right)

def postorder(start):
    if start == '.' :
        return

    # 부모의 자식은 2개씩 무조건.
    left = trees[start][0]
    right = trees[start][1]

    postorder(left)
    postorder(right)
    print(start,end='')

preorder(start)
print()
inorder(start)
print()
postorder(start)



# 220801
# import sys
# read = sys.stdin.readline
#
# N = int(read())
#
# graph = {}
# for i in range(1,N+1):
#     root,left,right = read().split()
#     graph[root] = [left,right]
#
# def preorder(trees,now):
#     print(now,end='')
#
#     left = trees[now][0]
#     right = trees[now][1]
#     # left 순회
#     if left != '.' :
#         preorder(trees,left)
#     # right 순회
#     if right != '.' :
#         preorder(trees,right)
#
# # print의 순서만 바꿈으로써 이게 다 되네..;
# # 아직은 잘 모르겠다.
# def inorder(trees,now):
#
#     left = trees[now][0]
#     right = trees[now][1]
#     # left 순회
#     if left != '.' :
#         inorder(trees,left)
#     print(now,end='')
#     # right 순회
#     if right != '.' :
#         inorder(trees,right)
#
# def postorder(trees,now):
#
#     left = trees[now][0]
#     right = trees[now][1]
#     # left 순회
#     if left != '.' :
#         postorder(trees,left)
#     # right 순회
#     if right != '.' :
#         postorder(trees,right)
#     print(now,end='')
#
# preorder(graph, 'A')
# print()
# inorder(graph,'A')
# print()
# postorder(graph,'A')
