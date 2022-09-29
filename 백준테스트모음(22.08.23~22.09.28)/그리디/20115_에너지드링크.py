import sys
read = sys.stdin.readline

"""
1. 서로 다른 에너지 드링크를 합친다.
2. 하나를 다른쪽에 다 붓는데, 양의 절반을 흘린다.
3. 빈 에너지 드링크는 버린다.
4. 1~3 반복

에너지 드링크의 양을 최대로 하기
"""
from fractions import Fraction
N = int(read())
drinks = list(map(int,read().split()))
drinks.sort(reverse=True)
max_d = drinks[0]
results = max_d + float(Fraction(sum(drinks[1:]),2))
print("{0:.4f}".format(results))
