dict_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
              '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z'}
answer = ""
data = input().split("|")
for i in data:
    word = i.strip()
    for d in dict_morse:
        if len(word) <= 3:
            if d == word:
                answer += ''.join(dict_morse[d])
                answer += ''.join(" ")
                break
            else:
                continue
        else:
            for dd in word.split(' '):
                answer += ''.join(dict_morse[dd])
        answer += ''.join(" ")
        break
print(answer)
