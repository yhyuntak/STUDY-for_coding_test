N = int(input())
card_list = [0]
card_list += list(map(int,input().split()))
dp_table = [0]*(N+1)
dp_table[1] = card_list[1]

for n in range(2,N+1):
    temp = card_list[n]
    for p in range(1,n):
        temp = max(temp,card_list[p]+dp_table[n-p])
    dp_table[n] = temp

print(dp_table[-1])
