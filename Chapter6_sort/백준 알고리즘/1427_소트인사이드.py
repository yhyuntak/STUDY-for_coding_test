import sys
read = sys.stdin.readline

N = read().split()
N = N[0]
N_array = []

for i in range(len(N)):
    N_array.append(int(N[i]))

N_array.sort(reverse=True)

for j in range(len(N)):
    print(N_array[j],end='')