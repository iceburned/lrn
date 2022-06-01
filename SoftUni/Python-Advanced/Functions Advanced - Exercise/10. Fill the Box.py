def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    temp_sum = 0
    temp_left = 0
    flag = True

    for i in args:

        if i == "Finish":
            break
        else:
            if flag:
                temp_sum += i

        if not flag:
            temp_left += i

        if temp_sum >= box_size and flag:
            temp_sum = temp_sum - i
            temp_left = i - (box_size - temp_sum)
            flag = False

    if flag:
        place_left = box_size - temp_sum
        return f"There is free space in the box. You could put {place_left} more cubes."
    else:
        return f"No more free space! You have {temp_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))