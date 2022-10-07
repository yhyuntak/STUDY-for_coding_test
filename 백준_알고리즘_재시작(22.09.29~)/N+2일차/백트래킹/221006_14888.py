import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_val = -10e9
min_val = 10e9

def dfs(depth,total,plus,minus,multiply,divide):
    if depth == N-1 :
        global max_val,min_val
        max_val = max(max_val,total)
        min_val = min(min_val,total)
        return

    if plus :
        dfs(depth+1,total+num[depth+1],plus-1,minus,multiply,divide)
    if minus :
        dfs(depth+1,total-num[depth+1],plus,minus-1,multiply,divide)
    if multiply :
        dfs(depth+1,total*num[depth+1],plus,minus,multiply-1,divide)
    if divide :
        dfs(depth+1,int(total/num[depth+1]),plus,minus,multiply,divide-1)

dfs(0,num[0],op[0],op[1],op[2],op[3])

print(max_val)
print(min_val)