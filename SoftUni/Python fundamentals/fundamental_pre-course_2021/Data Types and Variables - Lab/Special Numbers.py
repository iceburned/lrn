n = int(input())
d = 0
for _ in range(1, n + 1):
     a = _ // 10
     b = _ % 10
     c = a + b
     if _ < 10:
          if 5 == _ or 7 == _:
               print(f'{_} -> True')
          else:
               print(f'{_} -> False')
     else:
          if c == 5 or c == 7 or c == 11:
               print(f'{_} -> True')
          else:
               print(f'{_} -> False')
