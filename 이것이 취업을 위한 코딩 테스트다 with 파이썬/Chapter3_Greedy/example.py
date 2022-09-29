import numpy as np

N = 1260
coin_vals = [500,100,50,10]
coin_num = []
for coin in coin_vals :
    temp = N//coin
    coin_num.append(temp)
    N -= temp*coin

print(coin_num)