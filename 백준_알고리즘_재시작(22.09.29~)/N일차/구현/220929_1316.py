N = int(input())

num_words = 0
for _ in range(N):
    word_dict = {}
    word = input()
    switch = 1
    before_w = word[0]
    word_dict[before_w] = 1
    for now_idx in range(1,len(word)) :
        if before_w == word[now_idx] :
            continue
        elif before_w != word[now_idx] : # 이전 단어와 현재 단어가 다를 때,
            # 현재 단어가 존재하지 않으면 1 추가하면서 before_w 갱신
            if word_dict.get(word[now_idx]) is None :
                word_dict[word[now_idx]] = 1
                before_w = word[now_idx]
            else :
                # 존재하면 스위치 off하고 for문 종료
                    switch = 0
                    break
    num_words += switch
print(num_words)

# 10분 걸림
