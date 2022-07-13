lst = input()
vowels = ['a', 'o', 'u', 'e', 'i']
print(''.join([_ for _ in lst if _.lower() not in vowels]))
