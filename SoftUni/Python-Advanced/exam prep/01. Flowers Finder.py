from collections import deque

vowels = deque(_ for _ in input().split())
consonants = deque(_ for _ in input().split())
words = ["rose", "tulip", "lotus", "daffodil"]
flag  =True
while vowels and consonants and flag:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    # words = words.pop()
    for i in range(4):
        if vowel in words[i]:
            words[i] = words[i].replace(vowel, '', 1)
    for ii in range(4):
        if consonant in words[ii]:
            words[ii] = words[ii].replace(consonant, '', 1)
    if not all(filter(lambda x: x == '', words)):
        break


# da se razgleda
# matrixx = [[f"{chr(col+97)}{row+1}" for col in range(8)] for row in range(7,-1,-1)]
# [0:10]
# if capture:
#     print(f"Game over! {final} win, capture on {matrixx[w_row][w_col]}.")
# elif promoted:
#     print(f"Game over! {final} pawn is promoted to a queen at {matrixx[w_row][w_col]}.")