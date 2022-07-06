def find_parent(parent,x):
    if parent[x] != x : # 루트 노드랑 말 그대로 자신의 제일 첫 조상을 의미한다고 생각하면 될듯.
        # 그래서 내가 조상님이 아니라면 조상을 찾기위해 재귀 코드를 실행하자.
        parent[x] = find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b

v,e = map(int,input().split())
parent = [i for i in range(0,v+1)]

cycle = False

for i in range(3):
    a,b = map(int,input().split())

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else :
        union_parent(parent,a,b)