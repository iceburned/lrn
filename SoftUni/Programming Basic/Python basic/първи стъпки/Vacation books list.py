papers = int(input())
papers_per_hours = int(input())
days = float(input())

hours_for_reading = int((papers / papers_per_hours) / days)

print(hours_for_reading)
