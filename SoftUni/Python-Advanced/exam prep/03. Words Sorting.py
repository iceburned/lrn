def words_sorting(*args):
    dkt = {_: 0 for _ in args if _ != ''}
    for k in dkt:
        for el in k:
            dkt[k] += ord(el)
    if sum(dkt.values()) % 2 == 0:
        dkt = sorted(dkt.items(), key=lambda x: x[0])
    else:
        dkt = sorted(dkt.items(), key=lambda x: -x[1])

    return '\n'.join([f"{k} - {v}" for k, v in dkt])

print(
    words_sorting(
        'escape',
        'charm',
        'mythology',
        ''
  ))

print("-----------------")

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print("-----------------")

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))