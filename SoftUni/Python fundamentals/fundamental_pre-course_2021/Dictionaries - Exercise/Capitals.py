dkt = input().split(", ")
dkt1 = input().split(", ")
my_dict = {k: v for k, v in zip(dkt, dkt1)}
for key, value in my_dict.items():
    print(f"{key} -> {value}")
