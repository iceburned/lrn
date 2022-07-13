data = [_ for _ in input()]
bonus = 0
for i in range(len(data)):
    if data[i] == ">":
        counter = data[i + 1]
        if counter.isdigit():
            counter = int(counter)
            if counter > 0:
                counter += bonus
            else:
                counter += bonus + 1
            if (counter + i) > len(data):
                counter = len(data) - i - 1
            for ii in range(1, counter + 1):
                bonus = 0
                if data[i + ii] != ">":
                    data[i + ii] = "None"
                else:
                    bonus += abs(counter - (ii + 1))
                    break
for h in data:
    if not h == "None":
        print(h, end="")
