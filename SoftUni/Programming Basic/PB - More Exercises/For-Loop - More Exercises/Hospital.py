period = int(input())

patients_unchecked = 0
patients_checked = 0
doctors = 7
days = 0

for _ in range(period):
    patients = int(input())
    days += 1
    if days % 3 == 0 and patients_unchecked > patients_checked:
        doctors += 1
    if patients > 7:
        patients_unchecked += (patients - doctors)
        patients_checked += doctors
    else:
        patients_checked += patients
print(f"Treated patients: {patients_checked}.")
print(f"Untreated patients: {patients_unchecked}.")
