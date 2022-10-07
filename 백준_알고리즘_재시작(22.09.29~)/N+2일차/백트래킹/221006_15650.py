N,M = map(int,input().split())
now_comb = []

def dfs():
    if len(now_comb) == M :
        print(*now_comb)
        return

    for j in range(now_comb[-1]+1,N+1):
        now_comb.append(j)
        dfs()
        now_comb.pop()

for i in range(1,N+1):
    now_comb.append(i)
    dfs()
    now_comb.pop()