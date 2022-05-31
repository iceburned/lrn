def sorting_cheeses(**kwargs):
    chease = kwargs
    asd = sorted(chease.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for k, v in asd:
        result.append(k)
        result.extend(sorted(v, reverse=True))

    return '\n'.join([str(_) for _ in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)