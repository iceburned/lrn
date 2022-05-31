def even_odd_filter(**kwargs):
    def odd(lst):
        return [_ for _ in lst if _ % 2 != 0]

    def even(lst):
        return [_ for _ in lst if _ % 2 == 0]

    dkt = kwargs
    for i in dkt.items():
        if i[0] == "odd":
            dkt["odd"] = odd(i[1])
        elif i[0] == "even":
            dkt["even"] = even(i[1])

    return dict(sorted(dkt.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))