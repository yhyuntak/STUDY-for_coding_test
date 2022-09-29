import sys
read = sys.stdin.readline

N,K = map(int,read().split())

coin_array = []
for i in range(N):
    coin_array.append(int(read()))

coin_array.reverse()

result = 0
for j in range(N):
    coin = coin_array[j]
    result += K // coin
    K = K % coin

    # print(coin,K,result)

print(result)