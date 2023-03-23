k = int(input())
for t in range(k):
    word_ = input()
    word_list = word_.split(' ')
    word_list = word_[::-1].split(' ')
    word_list.reverse()
    print(word_list)