def bar(num):
    n = num // 10
    string_bar = '..........'
    str_bar = string_bar.replace('.', '%', n)
    return str_bar


num = int(input())
answer = bar(num)
if num == 100:
    print(f'100% Complete!\n[{answer}]')
else:
    print(f'{num}% [{answer}]\nStill loading...')
