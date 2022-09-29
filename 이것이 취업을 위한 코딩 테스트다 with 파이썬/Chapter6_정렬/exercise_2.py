n = int(input())

array = []

for i in range(n):
    array.append(list(input().split()))

def criterion(array):
    return array[1]
result = sorted(array,key=criterion)



for name,_ in result:
    print(name,end=' ')