judges = int(input())

average = 0
average1 = 0
scores = 0
count = 0
while True:
    presentation = input()
    if presentation == "Finish":
        break
    for n in range(0, judges):
        s = float(input())
        scores += s
        count += 1
    average += scores / judges
    average1 += scores
    print(f'{presentation} - {(average):.2f}.')
    scores = 0
    average = 0
print(f"Student's final assessment is {(average1 / count):.2f}.")
