year = int(input())

# (1) 4의 배수이고 100의 배수가 아닌 경우
# (2) 400의 배수인 경우

condition_four = year % 4 == 0
condition_not_one_hundred = year % 100 != 0
condition_four_hundred = year % 400 == 0

if (condition_four and condition_not_one_hundred) or condition_four_hundred :
    print(1)
else :
    print(0)
    