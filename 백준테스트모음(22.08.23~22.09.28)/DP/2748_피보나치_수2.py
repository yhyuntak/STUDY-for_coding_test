

#220916

N = int(input())

d = [0 for _ in range(N+1)]
d[1] = 1

for i in range(2,N+1):
    d[i] = d[i-1]+d[i-2]

print(d[-1])