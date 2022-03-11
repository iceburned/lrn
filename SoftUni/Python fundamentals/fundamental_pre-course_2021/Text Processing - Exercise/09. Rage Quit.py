data = [_ for _ in input()]
new_string = []
index = 0
for i in range(len(data)):
    if data[i].isdigit():
        num = 0
        if i < len(data) - 1:
            if data[i + 1].isdigit():
                num = int(data[i]+data[i+1])
        else:
            num = int(data[i])
        new_string.append((data[index:i]) * num)
        index = i+1
        i += 1
answer_str = []
for ss in new_string:
    answer_str += ss
answer = ''
for ii in answer_str:
    answer += ''.join(ii).upper()
set_answer = len(set(answer))
print(f"Unique symbols used: {len(set(answer))}\n{answer}")
