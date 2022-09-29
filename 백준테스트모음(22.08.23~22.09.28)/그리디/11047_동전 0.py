import sys
read = sys.stdin.readline

"""
동전이 N종류 있고, 동전들을 적절히 사용해서 가치의 합을 K로 만들되, 동전을 최소로 사용하자.

해법 : 큰거부터 나누자.
"""

N,K = map(int,read().split())
coins = []
for _ in range(N):
    # 코인의 개수를 줄이기 위해서 최대한 저장을 덜 하자.
    temp = int(read())
    if temp <= K :
        coins.append(temp)

num_coins = 0
coin_idx = 0
while K != 0 :
    temp_idx = -1 - coin_idx
    coin = coins[temp_idx]

    num_coins += (K // coin)
    K -= coin*(K//coin)

    coin_idx += 1
print(num_coins)