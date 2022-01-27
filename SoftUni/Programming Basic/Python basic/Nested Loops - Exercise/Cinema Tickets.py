movie_name = input()

count_tickets = 0
count_places_per_movie = 0
standard_ticket = 0
standard_ticket_per_movie = 0
kid_ticket = 0
kid_ticket_per_movie = 0
student_ticket = 0
student_ticket_per_movie = 0
type_ticket = ''
free_places = 0
while True:

    free_places = free_places_used = int(input())
    while True:
        type_ticket = input()

        if type_ticket == 'End':
            pass
        elif type_ticket != 'Finish':

            count_tickets += 1
            count_places_per_movie += 1
            free_places_used -= 1
            if type_ticket == 'standard':
                standard_ticket += 1
                standard_ticket_per_movie += 1
            elif type_ticket == 'kid':
                kid_ticket += 1
                kid_ticket_per_movie += 1
            elif type_ticket == 'student':
                student_ticket += 1
                student_ticket_per_movie += 1
        if type_ticket == 'End' or type_ticket == 'Finish' or free_places_used == 0:
            sum_sum = ((student_ticket_per_movie + standard_ticket_per_movie +
                        kid_ticket_per_movie) / free_places) * 100
            print(f"{movie_name} - {sum_sum:.2f}% full.")
            break

    if type_ticket == 'Finish':
        break
    movie_name = input()
    if movie_name == 'Finish':
        break
    count_places_per_movie = 0
    standard_ticket_per_movie = 0
    student_ticket_per_movie = 0
    kid_ticket_per_movie = 0

total_tickets_student = (student_ticket / count_tickets) * 100
total_tickets_standard = (standard_ticket / count_tickets) * 100
total_tickets_kid = (kid_ticket / count_tickets) * 100
print(f"Total tickets: {count_tickets}\n{total_tickets_student:.2f}% student tickets.\n"
      f"{total_tickets_standard:.2f}% standard tickets.\n{total_tickets_kid:.2f}% kids tickets.")