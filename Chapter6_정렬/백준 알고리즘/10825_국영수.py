import sys
read = sys.stdin.readline

N = int(input())
table = []
for _ in range(N):
    name,a,b,c = list(read().split())
    table.append([name,int(a),int(b),int(c)])

table.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(table[i][0])
