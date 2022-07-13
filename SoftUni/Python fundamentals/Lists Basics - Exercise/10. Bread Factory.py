# event_string = input().split('|')
# baker = [100, 100]  # [0] = energy, [1] = coins
#
#
# def rest(energy_, value_):
#     energy_ += value_
#     if energy_ > 100:
#         value_ -= energy_ - 100
#         energy_ = 100
#     print(f"You gained {value_} energy.")
#     print(f"Current energy: {energy_}.")
#     return energy_
#
#
# def order(energy_, coins_, value_):
#     if energy_ >= 30:
#         energy_ -= 30
#         coins_ += value_
#         print(f'You earned {coins_} coins.')
#     else:
#         energy_ += 50
#         print(f"You had to rest!")
#     return [energy_, coins_]
#
#
# def buy(item_, value_, coins_):
#     if coins_ >= value_:
#         coins_ -= value_
#         print(f"You bought {item_}.")
#     else:
#         print(f"Closed! Cannot afford {item_}.")
#         quit(0)
#     return coins_
#
#
# def actions(baker_, event_, value_):
#     if event_ == "rest":
#         baker_[0] = rest(baker_[0], value_)
#     elif event_ == "order":
#         baker_ = order(baker_[0], baker_[1], value_)
#     else:
#         baker_[1] = buy(event_, value_, baker_[1])
#     return baker_
#
#
# for e in event_string:
#     event_split = e.split('-')
#     event = event_split[0]
#     value = int(event_split[1])
#     baker = actions(baker, event, value)

# rest-2|order-10|eggs-100|rest-10
event_string = input().split('|')
energy = 100
coins = 100
close_condition = False
for e in event_string:
    event_split = e.split('-')
    event = event_split[0]
    value = int(event_split[1])
    if event == 'rest':
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            close_condition = True
            break
if not close_condition:
    print(f"Day completed!")
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
