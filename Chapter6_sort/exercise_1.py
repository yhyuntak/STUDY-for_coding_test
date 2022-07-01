n = int(input())

array = []

for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)

for _ in range(n):
    print(array[_],end=' ')
