mtx = []
for _ in range(int(input())):
    mtx.append(list(input()))
srch_item = input()
tpl = ()
for i in range((len(mtx))):
    if srch_item in mtx[i]:
        num = mtx[i].index(srch_item)
        tpl = (i, num)
        break
print(tpl if tpl else f"{srch_item} does not occur in the matrix")
