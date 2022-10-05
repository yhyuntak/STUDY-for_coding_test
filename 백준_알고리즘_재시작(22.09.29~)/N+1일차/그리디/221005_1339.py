N = int(input())


# 각 단어들의 최대 길이가 8이니까 그 공백만큼 앞에 뭔가를 채워줘야할듯.
array = []
for _ in range(N):
    temp = input()
    temp_arr = [ '.' for a in range(8-len(temp))]
    temp = ''.join(temp_arr) + temp
    array.append(temp)

dict_ = {}

for i in range(8):
    # 모든 단어 숫자를 하나씩 확인.
    for a in array :
        if a[i] == '.' :
            continue
        else :
            try: dict_[a[i]] += 10 ** (7-i)
            except : dict_[a[i]] = 10**(7-i)

sums = 0
sort_list = sorted(list(dict_.items()),key=lambda x:-x[1])
value = 9
for _,temp in sort_list:
    sums += temp*value
    value-=1
print(sums)