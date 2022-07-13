num = int(input())
while True:
    num += 1
    num1 = str(num)
    if len(set(num1)) == len(num1):
        print(num)
        break
