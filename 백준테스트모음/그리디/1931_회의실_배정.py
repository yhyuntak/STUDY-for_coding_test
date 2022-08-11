import sys
read = sys.stdin.readline

N = int(read())
time_table = []
times = []
for _ in range(N):
    times.append(list(map(int,read().split())))

times.sort(key=lambda x:(x[1],x[0]))

time_table = [times[0]]
for i in range(1,len(times)):
    start,end = times[i]
    if start >= time_table[-1][1] :
        time_table.append(times[i])
print(len(time_table))