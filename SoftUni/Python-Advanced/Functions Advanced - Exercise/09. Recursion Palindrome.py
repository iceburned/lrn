def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    left_part = word[idx]
    right_part = word[len(word) - 1 - idx]
    if left_part != right_part:
        return f"{word} is not a palindrome"
    return palindrome(word, idx + 1)



print(palindrome("abcba", 0))