def add_stop(stop, index, place):
    index_num = int(index)
    if 0 <= index_num <= len(stop):
        stop = stop[:index_num] + place + stop[index_num:]
    print(stop)
    return stop


def remove_stop(stop, strt_indx, stop_indx):
    strt_indx = int(strt_indx)
    stop_indx = int(stop_indx)
    if 0 <= strt_indx <= len(stop) >= stop_indx:
        stop = stop[:strt_indx] + stop[stop_indx + 1:]
    print(stop)
    return stop


def switch_stop(stop, old_str, new_str):
    stop = stop.replace(old_str, new_str)
    print(stop)
    return stop


stops = input()
action = input()
while not action == "Travel":
    action = action.split(":")
    if "Add Stop" == action[0]:
        stops = add_stop(stops, action[1], action[2])
    elif "Remove Stop" == action[0]:
        stops = remove_stop(stops, action[1], action[2])
    elif "Switch" == action[0]:
        stops = switch_stop(stops, action[1], action[2])
    action = input()
print(f"Ready for world tour! Planned stops: {stops}")
