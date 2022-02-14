def sum_sum(a):
    if all(a):
        negative = [_ for _ in a if abs(_) != _]
        if len(negative) % 2 != 0:
           return 'negative'
        else:
           return 'positive'
    return 'zero'


num = [int(input()) for _ in range(3)]
print(sum_sum(num))
