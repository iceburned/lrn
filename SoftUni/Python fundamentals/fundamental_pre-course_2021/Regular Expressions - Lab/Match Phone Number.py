import re
data = input()
reg_code = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"
answer = re.finditer(reg_code, data)
valid_answer = [_.group() for _ in answer]
print(", ".join(valid_answer))
