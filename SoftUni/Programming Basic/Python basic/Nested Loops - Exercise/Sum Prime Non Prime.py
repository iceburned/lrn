prime = 0
non_prime = 0
flag = False
while True:
    num = input()
    if num == "stop":
        break
    num = int(num)
    if num < 0:
        print('Number is negative.')
    else:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = True
            if flag:
                flag = False
                non_prime += num
            else:
                prime += num
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
