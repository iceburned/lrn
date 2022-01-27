first_letter = input()
second_letter = input()
third_letter = input()

word_str = ''
count = 0
for a in range(ord(first_letter), ord(second_letter)+1):
    word_str += chr(a)

for i in word_str:
    for j in word_str:
        for k in word_str:
            sum_sum = i + j + k
            if third_letter in sum_sum:
                pass
            else:
                print(sum_sum, end=' ')
                count += 1
print(count, end=' ')
