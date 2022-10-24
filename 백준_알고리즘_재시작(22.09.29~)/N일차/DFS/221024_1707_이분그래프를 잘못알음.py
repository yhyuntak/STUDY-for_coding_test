from copy import deepcopy as dp

def dfs(parent,visit,return_bool):
    for child in trees[parent] :

        if not return_bool : # 이게 작동된다면 순환 트리인 것이므로 그대로 순환 트리라는 것을 알려주면됨.
            return return_bool

        if visit[child] == 0 :
            visit[child] = 1
            # pop으로 서로간의 간선을 삭제해버리기.
            trees[parent].pop(trees[parent].index(child))
            trees[child].pop(trees[child].index(parent))

            # 정상작동한다면 bool은 True로 계속 진행될 것.
            return_bool = dfs(child,visit,return_bool)

        # 지금 pop으로 연결을 끊어놨기 때문에, 순환트리가 아니라면 다신 방문했던 곳으로 갈 수 없다.
        # 근데 visited == 1 을 만난다는 것은 순환인 것이므로 종료.
        else :
            return False

    return return_bool

K = int(input())
for k in range(1,K+1):
    V,E = map(int,input().split())
    trees = [[] for _ in range(V+1)] # 정점의 개수만큼 형성
    for e in range(E):
        # 서로 양방향성을 갖도록 만들고
        a,b = map(int,input().split())
        trees[a].append(b)
        trees[b].append(a)

    visited = [0 for _ in range(V + 1)]

    for s in range(1,V+1): # 모든 노드를 탐색해야함.

        cp_visited = dp(visited)

        # 순환이 없는 트리인지만 확인하면 반드시 이분 그래프로 만들 수 있다.
        # 깊이 탐색을 하면서, 자신의 부모 노드가 아닌데 방문한 곳을 만난다면 순환트리이다 -> 핵심
        cp_visited[s] = 1

        if not dfs(s,cp_visited,True) :
            print("NO")
            break
    else :
        print("YES") # 무사히 for문을 통과한다면 yes




