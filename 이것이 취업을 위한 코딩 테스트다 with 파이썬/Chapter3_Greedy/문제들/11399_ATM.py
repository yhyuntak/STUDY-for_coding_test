n = int(input())
array = list(map(int,input().split()))
array.sort()

summation = []
for idx,_ in enumerate(array):
    summation.append(sum(array[:idx+1]))
print(sum(summation))
