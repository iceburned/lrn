text_file = open("text.txt", "r")  # open file text.txt
flag = 0  # counter for even lines
for line in text_file:
    if flag % 2 == 0:
        for s in line:
            if s in ("-", ",", ".", "!", "?"):  # checker for element
                line = line.replace(s, "@")
        line = line.split()
        print(*line[::-1])
    flag += 1
text_file.close()  # close file text.txt


'''
output:
fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@
'''