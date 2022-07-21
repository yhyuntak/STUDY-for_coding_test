S = input()
array = []
for i in range(len(S)):
    array.append(S[i:])
array.sort()
for j in range(len(array)):
    print(array[j])
