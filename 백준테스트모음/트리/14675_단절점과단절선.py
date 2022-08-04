import sys
read = sys.stdin.readline
N = int(read())
trees = dict()
for i in range(1,N+1):
    trees[i] = []

for _ in range(N-1):
    a,b = map(int,read().split())
    trees[a].append(b)
    trees[b].append(a)

def dfs(trees,start,check_tree):
    node = trees[start]
    if len(node) == 0 : # 노드가 연결된게 없으면 종료
        return check_tree
    for n in node : # 연결된게 있으면 돌아가야지.
        check_tree = dfs(trees,n,check_tree) + [n]
    return check_tree

q = int(read())
for _ in range(q):
    t,k = map(int,read().split())
    # t가 1은 단절점 확인
    # 단절점은 해당 노드가 간선을 2개 이상 갖고 있으면 된다.
    if t==1 :
        if len(trees[k])>=2 :
            print("yes")
        else :
            print("no")
    # t가 2는 단절선확인
    # 간선을 끊으면 무조건 트리가 2개이상 형성될 수 밖에 없다.
    else :
        print("yes")