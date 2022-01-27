import re
data_str = input()
reg_code = r"\b(?P<day>\d{2})(?P<separator>[-/\.])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"
answers = re.findall(reg_code, data_str)
for answer in answers:
    print(f"Day: {answer[0]}, Month: {answer[2]}, Year: {answer[3]}")
# drugo reshenie
# answers = re.finditer(reg_code, data_str)
# for date in answers:
#     current_date = date.groupdict()
#     print(f"Day: {current_date['day']}, Month: {current_date['month']}, Year: {current_date['year']}")