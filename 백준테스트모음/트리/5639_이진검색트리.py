



# 220801
# import sys
# sys.setrecursionlimit(10**6)
#
#
# preorder = []
#
# while True :
#     try :
#         preorder.append(int(sys.stdin.readline()))
#     except :
#         break
#
#
# def postorder(start,end):
#     if start >= end :
#         return
#     root = preorder[start]
#     div = end
#     # 현재 노드에서 갈리는 지점 찾기.
#     for i in range(start+1,end):
#         if root < preorder[i] :
#             # 현재 노드보다 큰것이 있다면 여기가 분기점
#             div = i
#             break
#     # 여기서 좌 우로 DFS를 진행
#     # 순서는 후위순회이므로 왼->오->루트 이다.
#     # 따라서 루트의 출력을 제일 마지막에 해주면됨
#     postorder(start+1,div)
#     postorder(div,end)
#     print(root)
#
# postorder(0,len(preorder))
#
