def kwargs_length(**kwargs):
    dkt = kwargs
    return len(dkt)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

dictionary = {}

print(kwargs_length(**dictionary))