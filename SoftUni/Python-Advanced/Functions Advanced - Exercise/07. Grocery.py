def grocery_store(**kwargs):
    sorted_dict = [f'{k}: {v}' for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(sorted_dict)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))