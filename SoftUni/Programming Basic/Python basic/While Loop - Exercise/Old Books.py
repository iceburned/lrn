searchred_book = input()

rotated_books = input()
count = 0
while searchred_book != rotated_books:
    rotated_books = input()
    count += 1
    if rotated_books == "No More Books":
        print("The book you search is not here!")
        print("You checked " + str(count) + " books.")
        break

else:
    print("You checked " + str(count) + " books and found it.")
