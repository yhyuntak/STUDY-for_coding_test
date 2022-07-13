N = int(input())
word_array = []

for _ in range(N):
    word = input()
    if not word in word_array :
        word_array.append(word)

# 먼저 사전적 정의로 오름차순 정렬을 적용하자.
word_array.sort()

# 그리고 길이별로 오름차순 정렬을 하면 된다.
word_array.sort(key= lambda x:len(x))

for i in range(len(word_array)):
    print(word_array[i])