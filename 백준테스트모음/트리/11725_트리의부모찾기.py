import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(read())
tree = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,read().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start,tree,parents):
    # start 노드에 연결된 vertex들을 확인하자.
    for i in tree[start]:
        if parents[i] == 0 : # visited의 역할도 겸해준다.
            parents[i] = start
            DFS(i,tree,parents)

DFS(1,tree,parents)

for j in range(2,N+1):
    print(parents[j])