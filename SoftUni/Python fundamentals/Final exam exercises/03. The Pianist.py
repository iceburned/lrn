def add(my_dict, piece_add, composer_add, key_add):
    if piece_add in my_dict:
        print(f"{piece_add} is already in the collection!")
    else:
        my_dict.update({piece_add: {"composer": composer_add, "key": key_add}})
        print(f"{piece_add} by {composer_add} in {key_add} added to the collection!")
    return my_dict


def remove(my_dict, piece_remove):
    if piece_remove in my_dict:
        my_dict.pop(piece_remove)
        print(f"Successfully removed {piece_remove}!")
    else:
        print(f"Invalid operation! {piece_remove} does not exist in the collection.")
    return my_dict


def changekey(my_dict, piece_new, key_new):
    if piece_new in my_dict:
        my_dict[piece_new]["key"] = key_new
        print(f"Changed the key of {piece_new} to {key_new}!")
    else:
        print(f"Invalid operation! {piece_new} does not exist in the collection.")
    return my_dict


dkt = {}
for _ in range(int(input())):
    piece, composer, key = input().split("|")
    if piece not in dkt:
        dkt.update({piece: {"composer": '', "key": ''}})
    dkt[piece]["composer"] = composer
    dkt[piece]["key"] = key
command = input()
while not command == "Stop":
    if command.startswith("Add"):
        comm, p, c, k = command.split("|")
        dkt = add(dkt, p, c, k)
    elif command.startswith("Remove"):
        comm, p = command.split("|")
        dkt = remove(dkt, p)
    elif command.startswith("ChangeKey"):
        comm, p, k = command.split("|")
        dkt = changekey(dkt, p, k)
    command = input()
for i in dkt:
    print(f"{i} -> Composer: {dkt[i]['composer']}, Key: {dkt[i]['key']}")