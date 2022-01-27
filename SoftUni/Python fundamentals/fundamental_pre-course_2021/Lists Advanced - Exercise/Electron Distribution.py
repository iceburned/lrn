num = int(input())
lst = []
for i in range(1, num + 1):
    sum_sum = (2 * (i ** 2))
    sum_num = num - sum(lst)
    if 18 <= sum_sum:
        lst.append(18)
    else:
        lst.append(2 * pow(i, 2))
    if sum(lst) > num:
        lst.pop(-1)
        if sum_num > 0:
            lst.append(sum_num)
        break
print(lst)

total_electrons = int(input())
electron_config = []
current_layer = 1
while total_electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)
    if total_electrons >= current_layer_electrons:
        electron_config.append(current_layer_electrons)
    else:
        electron_config.append(total_electrons)
    total_electrons -= current_layer_electrons
    current_layer += 1
electron_config_str = [str(layer) for layer in electron_config]
print(electron_config)
