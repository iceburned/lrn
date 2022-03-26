data = [_ for _ in input()]
new_string = ''
temp_str = ''
for i in data:
    if i.isdigit():
        new_string += (temp_str * int(i)).upper()
        temp_str = ''
    else:
        temp_str += ''.join(i)

set_answer = len(set(new_string))
print(f"Unique symbols used: {set_answer}\n{new_string}")
