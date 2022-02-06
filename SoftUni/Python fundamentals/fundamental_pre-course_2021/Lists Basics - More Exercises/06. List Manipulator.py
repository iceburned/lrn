'''
1 10 100 1000
exchange 10
first 2 odd
last 4 odd
end
'''


def exchange(string_, lst_):
    string_split = string_.split(' ')
    str_spl = int(string_split[1])
    if 0 <= str_spl <= len(lst_):
        lst_ = lst[str_spl+1:] + lst[:str_spl+1]
        return lst_
    else:
        print("Invalid index")
        return lst_


def odd(lst_, flag_):
    count = []
    for i in lst_:
        if i % 2 != 0:
            count.append(i)
    if count:
        return count
    else:
        if flag_:
            return count


def even(lst_, flag_):
    count = []
    for i in lst_:
        if i % 2 == 0:
            count.append(i)
    if count:
        return count
    else:
        if flag_:
            return count


def max_value(string_, lst_, flag_):
    string_split = string_.split(' ')
    str_spl = string_split[1]
    if str_spl == 'odd':
        odd_value = odd(lst_, flag_)
        if odd_value:
            if string_split[0] == "max":
                count = lst_.index(max(odd_value))
                print(count)
            else:
                count = odd_value.index(max(odd_value))
                print(count)
        else:
            print("No matches")
    elif str_spl == 'even':
        even_value = even(lst_, flag_)
        if even_value:
            if string_split[0] == "max":
                count = lst_.index(max(even_value))
                print(count)
            else:
                count = even_value.index(max(even_value))
                print(count)
        else:
            print("No matches")


def min_value(string_, lst_, flag_):
    string_split = string_.split(' ')
    str_spl = string_split[1]
    if str_spl == 'odd':
        odd_value = odd(lst_, flag_)
        if odd_value:
            if string_split[0] == "max":
                count = lst_.index(min(odd_value))
                print(count)
            else:
                count = odd_value.index(min(odd_value))
                print(count)
        else:
            print("No matches")
    elif str_spl == 'even':
        even_value = even(lst_, flag_)
        if even_value:
            if string_split[0] == "max":
                count = lst_.index(min(even_value))
                print(count)
            else:
                count = even_value.index(min(even_value))
                print(count)
        else:
            print("No matches")


def first_value(string_, lst_, flag_):
    string_split = string_.split(' ')
    str_spl = string_split[2]
    ssc = int(string_split[1])
    if str_spl == 'odd':
        odd_value = odd(lst_, flag_)
        if odd_value:
            if len(lst_) >= ssc:
                count = odd_value[:ssc]
                print(count)
            else:
                print("Invalid count")
    elif str_spl == 'even':
        even_value = even(lst_, flag_)
        if even_value:
            if len(lst_) >= ssc:
                count = even_value[:ssc]
                print(count)
            else:
                print("Invalid count")
        else:
            print(even_value)


def last_value(string_, lst_, flag_):
    string_split = string_.split(' ')
    str_spl = string_split[2]
    ssc = int(string_split[1])
    if str_spl == 'odd':
        odd_value = odd(lst_, flag_)
        if odd_value:
            if len(lst_) >= ssc:
                count = odd_value[:ssc + 1]
                print(count)
            else:
                print("Invalid count")
    elif str_spl == 'even':
        even_value = even(lst_, flag_)
        if even_value:
            if len(lst_) >= ssc:
                count = even_value[:ssc + 1]
                print(count)
            else:
                print("Invalid count")
        else:
            print(even_value)


lst = input().split(' ')
lst = [int(_) for _ in lst]

command = input()
while not command == 'end':
    flag = False
    if "exchange" in command:
        lst = exchange(command, lst)
    elif "max" in command:
        max_value(command, lst, flag)
    elif "min" in command:
        min_value(command, lst, flag)
    elif "first" in command:
        flag = True
        first_value(command, lst, flag)
    elif "last" in command:
        flag = True
        last_value(command, lst, flag)
    command = input()
print(lst)



def center_point_a(a1, a2):
    if abs(a1) >= abs(a2):
        return a2
    else:
        return a1


def center_point_b(b1, b2):
    if abs(b1) >= abs(b2):
        return b2
    else:
        return b1


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

c1 = center_point_a(x1, x2)
c2 = center_point_b(y1, y2)
print(f'({c1}, {c2})')


#  reshena





def find_max_odd():
    max_odd = [el for el in list_of_integers if el % 2 != 0]
    if max_odd:
        found = (max(max_odd))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_max_even():
    max_even = [el for el in list_of_integers if el % 2 == 0]
    if max_even:
        found = (max(max_even))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_min_odd():
    min_odd = [el for el in list_of_integers if el % 2 != 0]
    if min_odd:
        found = (min(min_odd))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_min_even():
    min_even = [el for el in list_of_integers if el % 2 == 0]
    if min_even:
        found = (min(min_even))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def first():
    my_list = []
    if len(list_of_integers) < count_first:
        return "Invalid count"
    else:
        if even_odd == "even":
            my_list.extend([el for el in list_of_integers if el % 2 == 0])
            return my_list[:count_first]
        elif even_odd == "odd":
            my_list.extend([el for el in list_of_integers if el % 2 == 1])
            return my_list[:count_first]


def last():
    my_list = []
    if len(list_of_integers) < count_last:
        return "Invalid count"
    else:
        if even_odd == "even":
            my_list.extend([el for el in list_of_integers if el % 2 == 0])
            return my_list[-count_last:]

        elif even_odd == "odd":
            my_list.extend([el for el in list_of_integers if el % 2 == 1])
            return my_list[-count_last:]


list_of_integers = [int(el) for el in input().split()]
command = input()


while not command == "end":
    current_command = command.split()[0]
    if current_command == "exchange":
        index = int(command.split()[1])
        if 0 <= index < len(list_of_integers):
            list_of_integers = list_of_integers[index + 1:] + list_of_integers[:index + 1]

        else:
            print("Invalid index")

    elif current_command == "max":
        odd_or_even = command.split()[1]
        if odd_or_even == "odd":
            print(find_max_odd())

        elif odd_or_even == "even":
            print(find_max_even())

    elif current_command == "min":
        odd_even = command.split()[1]
        if odd_even == "odd":
            print(find_min_odd())

        elif odd_even == "even":
            print(find_min_even())

    elif current_command == "first":
        count_first = int(command.split()[1])
        even_odd = command.split()[2]
        print(first())

    elif current_command == "last":
        count_last = int(command.split()[1])
        even_odd = command.split()[2]
        print(last())

    command = input()
print(list_of_integers)