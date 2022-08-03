
from fractions  import Fraction
n,m = map(int,input().split())

dp_table = [1 for _ in range(n+1)]

for i in range(2,n+1):
    dp_table[i] = dp_table[i-1]*i


print(Fraction(dp_table[n],(dp_table[n-m]*dp_table[m])))
# from math import factorial as f
# print(Fraction(f(n),(f(n-m)*f(m))))
