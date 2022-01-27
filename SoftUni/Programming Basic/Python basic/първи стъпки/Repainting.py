nailon = (int(input()) + 2) * 1.50
paint = int(input())
paint += paint * 0.10
paint *= 14.50
thinner = int(input()) * 5.00
hours =  int(input())
sum_sum = nailon + paint + thinner + 0.40
workers = (sum_sum * 0.30) * hours
print(sum_sum + workers)


