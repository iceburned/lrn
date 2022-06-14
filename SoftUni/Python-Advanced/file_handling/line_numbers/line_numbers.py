text_file = open("text.txt", "r")   # input data from file
output_file = open("output_1.txt", "w")  # output data to file
flag = 1  # counter for every line in output_file
for line in text_file:
    line = line.replace("\n", "")  # removes annoying \n in end of line
    punctuations = ("-", ",", ".", "!", "?", "'", "(", ")", "{", "}", "[", "]", "_", ";", ":")
    punctuation_check = [1 for _ in line if _ in punctuations]  # create list for every punctuation mark
    punctuation_count = len(punctuation_check)  # sum punctuation marks to be used in output file
    letters = [1 for ss in line if ss not in punctuations and ss != ' ']  # create list for
    # a = []                                                              # letter in line
    # for ss in line:                               # same like list comprehension on line 9
    #     if ss not in punctuations and ss != ' ':  # but here is more readable
    #         a.append(1)
    letters_count = len(letters)  # letters count for output
    # write wanted data to output_1.txt
    output_file.write(f"Line {flag}: {line} ({letters_count})({punctuation_count})\n")
    flag += 1
text_file.close()  # close text.txt
output_file.close()  # close output_1.txt
