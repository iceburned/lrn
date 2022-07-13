def data_types(data, num):
    if data == 'int':
        return int(num) * 2
    elif data == 'real':
        return f'{(float(num) * 1.5):.2f}'
    elif data == 'string':
        return '$' + num + '$'


print(data_types(input(), input()))
