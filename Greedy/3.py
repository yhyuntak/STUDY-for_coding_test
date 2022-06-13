n,m = map(int,input().split())

result = 0
max_val = -1

for i in range(n):
    data = list(map(int,input().split()))
    max_val = max(min(data),max_val)
result = max_val
print(result)