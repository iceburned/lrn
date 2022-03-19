def takeodd(dat):
    dat = [_ for _ in dat]
    temp_str = ''
    for i in range(1, len(dat) + 1):
        if i % 2 == 0:
            temp_str += ''.join(dat[i - 1])
    return temp_str


def cut(dat, index, length):
    index = int(index)
    length = int(length)
    sub_str = dat[index:index + length]
    dat = dat.replace(sub_str, '', 1)
    return dat


def substitute(dat, substring, substitute):
    temp_dat = dat
    dat = dat.replace(substring, substitute)
    if temp_dat == dat:
        print("Nothing to replace!")
    else:
        print(dat)
    return dat


password = input()
data = input()
while not data == "Done":
    if data.startswith("TakeOdd"):
        password = takeodd(password)
        print(password)
    elif data.startswith("Cut"):
        comm, ind, leng = data.split(" ")
        password = cut(password, ind, leng)
        print(password)
    elif data.startswith("Substitute"):
        comm, string, stitute = data.split(" ")
        password = substitute(password, string, stitute)
    data = input()
print(f"Your password is: {password}")
