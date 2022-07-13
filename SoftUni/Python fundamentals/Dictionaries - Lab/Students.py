data = input()
dkt = {}
value1 = ''
value2 = ''
while ":" in data:
    value1, value2, key = data.split(':')
    if key not in dkt:
        dkt[key] = {}
    dkt[key][value2] = value1
    data = input()
searched_course = data
searched_course_name_split = searched_course.split('_')
searched_course = ' '.join(searched_course_name_split)
for course_name in dkt:
    if course_name == searched_course:
        for value2, value1 in dkt[course_name].items():
            print(f'{value1} - {value2}')
