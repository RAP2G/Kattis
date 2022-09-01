
inp = input()
split_inp = []
ans = inp

while int(ans) > 9:
    temp = 0
    for i in range(len(str(ans))):
        split_inp.append(int(str(ans)[i]))
    while 0 in split_inp:
        split_inp.remove(0)
    for i in range(len(split_inp)):
        if i > 0:
            temp = temp*split_inp[i]
        else:
            temp = split_inp[i]
    split_inp = []
    ans = temp
else:
    print(ans)
