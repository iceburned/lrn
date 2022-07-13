numbers = input().split()
sentence = input()
word = ''
for a in numbers:
    sum_sum = 0
    count1 = 0
    c1 = ''
    for b in a:
        sum_sum += int(b)
    while count1 <= sum_sum:
        for c in sentence:
            if count1 <= sum_sum:
                count1 += 1
                c1 = c
    word += word.join(c1)
    sentence = sentence.replace(c1, '', 1)
print(word)





