char = ""
n = 0
word = ""
total_word = ""

counter_n = 0
counter_o = 0
counter_c = 0
total_counter = 0

while True:
    char = input()

    if char == "End":
        print(str(total_word))
        break
    n = ord(char)

    if 65 <= n <= 122:

        if 91 <= n <= 96:
            continue
        if n == 110:
            counter_n += 1
            if counter_n > 1:
                word += chr(n)
        elif n == 111:
            counter_o += 1
            if counter_o > 1:
                word += chr(n)
        elif n == 99:
            counter_c += 1
            if counter_c > 1:
                word += chr(n)
        else:
            word += chr(n)

    if counter_n >= 1 and counter_c >= 1 and counter_o >= 1:

        total_word = total_word + word + " "
        counter_n = 0
        counter_o = 0
        counter_c = 0
        word = ""
