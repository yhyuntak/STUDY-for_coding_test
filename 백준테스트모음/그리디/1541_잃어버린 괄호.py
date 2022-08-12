import sys
read= sys.stdin.readline

input_text = str(read())
# 앞에 마이너스가 붙은것을 고려해 쪼개자
minus_split_text = input_text.split("-")
# 첫번째는 무조건 숫자니까 +가 있는 경우를 고려해서 더하자.
results = sum(map(int,minus_split_text[0].split("+")))

minus_results = 0
for a in range(1,len(minus_split_text)):
    minus_results += sum(map(int,minus_split_text[a].split("+")))
results -= minus_results

print(results)