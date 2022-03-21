def add(my_dict, piece, composer, key):
    if composer not in my_dict:
        my_dict[composer] = {}
        my_dict[composer][piece] = key
        if flag:
            print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        if piece in my_dict[composer]:
                print(f"{piece} is already in the collection!")
        else:
            if flag:
                print(f"{piece} by {composer} in {key} added to the collection!")
            my_dict[composer][piece] = key
    return my_dict


flag = False
dkt = {}
for i in range(int(input())):
    p, c, k = input().split("|")
    add(dkt, p, c, k)


def remove(my_dict, piece):
    for i in my_dict.values():
        if piece in i:
            i.pop(piece)
            for s in my_dict:
                if my_dict[s] == {}:
                    my_dict.pop(s)
                    print(f"Successfully removed {piece}!")
                    return my_dict
            else:
                print(f"Successfully removed {piece}!")
                return my_dict
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return my_dict


def change(my_dict, piece, new_key):
    for ss in my_dict:
        if piece in my_dict[ss]:
            my_dict[ss][piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
            return my_dict
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            return my_dict


data = input()
flag = True
while not data == "Stop":
    data = data.split("|")
    if "Add" in data:
        dkt = add(dkt, data[1], data[2], data[3])
    elif "Remove" in data:
        dkt = remove(dkt, data[1])
    elif "ChangeKey" in data:
        dkt = change(dkt, data[1], data[2])
    data =input()
for key, value in dkt.items():
    for k in value:
        print(f"{k} -> Composer: {key}, Key: {value[k]}")

# trqbva da podredq rechika po piece ne kompozitor