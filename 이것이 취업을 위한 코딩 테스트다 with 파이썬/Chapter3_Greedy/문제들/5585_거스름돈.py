N = int(input())
rest = 1000 - N
coin_array = [500,100,50,10,5,1]
cnt = 0
for i in range(len(coin_array)):
    cnt += rest // coin_array[i]
    rest = rest % coin_array[i]

print(cnt)