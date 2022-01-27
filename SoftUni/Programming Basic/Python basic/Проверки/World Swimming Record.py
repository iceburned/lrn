record_in_seconds = float(input())
length_in_meters = float(input())
time_in_seconds = float(input())
length = length_in_meters * time_in_seconds
slowing = length_in_meters // 15
slowing *= 12.5
total = length + slowing
if record_in_seconds > total:
    print(f" Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    miss = record_in_seconds - total
    print(f"No, he failed! He was {abs(miss):.2f} seconds slower.")
