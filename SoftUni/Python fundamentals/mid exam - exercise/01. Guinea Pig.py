food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
flag = True
for i in range(1, 31):
    if round(food) <= 0 or hay <= 0 or cover <= 0:
        flag = False
        break
    food -= 0.3
    if i % 2 == 0:
        index = food * 0.05
        hay -= index
    if i % 3 == 0:
        inx = weight / 3
        cover -= inx
if flag:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
