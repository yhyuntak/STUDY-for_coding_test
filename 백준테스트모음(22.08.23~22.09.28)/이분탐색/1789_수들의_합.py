# 이거 굉장히 쉽게 해결했었음.
"""
해결법은 간단함.
1부터 계속 더해나가다가 더이상 더하면 안될때까지 더한다.
그리고 S를 만족하려면 단순하게 현재 VAL의 최대값을 키우면된다.
그럼 개수 자체는 그대로 유지가 됨. 왜 이렇게 되냐면, N에 +1을 하려면 새로운 수를 추가해야되는데
추가하는 것은 불가능하기때문에 최대값을 늘림으로써 해결가능.

"""
import sys
read= sys.stdin.readline
S = int(read())

sums = 0
val = 0
while S-sums > 0:
    val += 1
    sums += val
if S-sums == 0 :
    print(val)
else :
    print(val-1)

# 4294967295