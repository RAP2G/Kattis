word = input()
inp = input()
lose_con = 0
win_con = 0
temp = set(word)
win_con = len(word)

for i in inp:
    if win_con > 0 and lose_con < 10:
        if i in temp:
            win_con -= 1
        else:
            lose_con += 1
    else:
        if win_con <= 0:
            print("WIN")
            break
        else:
            print("LOSE")
            break
