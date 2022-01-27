flowers = input()
count_flowers = int(input())
budget = int(input())
flowers_sum = 0
discount = 0

if flowers == "Roses":
    flowers_sum = count_flowers * 5
    if count_flowers > 80:
        discount = flowers_sum * 0.1
        flowers_sum -= discount
    else:
        pass
elif flowers == "Dahlias":
    flowers_sum = count_flowers * 3.80
    if count_flowers > 90:
        discount = flowers_sum * 0.15
        flowers_sum -= discount
    else:
        pass
elif flowers == "Tulips":
    flowers_sum = count_flowers * 2.80
    if count_flowers > 80:
        discount = flowers_sum * 0.15
        flowers_sum -= discount
    else:
        pass
elif flowers == "Narcissus":
    flowers_sum = count_flowers * 3
    if count_flowers < 120:
        discount = flowers_sum * 0.15
        flowers_sum += discount
    else:
        pass
elif flowers == "Gladiolus":
    flowers_sum = count_flowers * 2.50
    if count_flowers < 80:
        discount = flowers_sum * 0.2
        flowers_sum += discount
    else:
        pass
else:
    pass

sum_sum = abs(budget - flowers_sum)

if flowers_sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} "
          f"and {sum_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum_sum:.2f} leva more.")
