"""
input:
one
1
two
2
Search
one
Remove
two
End
"""

numbers_dictionary = {}   # temp dictionary
line = input()

# condition until Search
while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:                                     # ValueError
        print("The variable number must be an integer")
    line = input()

line = input()

# condition until Remove
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:                                        # KeyError
        print("Number does not exist in dictionary")
    line = input()

line = input()

# condition until End
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:                                        # KeyError
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)


'''
Output:
1
{'one': 1}
'''
