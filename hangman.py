

word = input()
inp = input()
lose_con = 0
win_con = 0


def count_letters(word: str):
    already_counted = []
    amount = 0
    for i in word:
        if word.count(i) > 1:
            if len(already_counted):
                for x in already_counted:
                    if x == i:
                        break
                else:
                    already_counted.append(i)
                    amount += 1
            else:
                already_counted.append(i)
                amount += 1
        else:
            amount += 1

    return amount


win_con = count_letters(word)
for i in inp:
    if win_con > 0 and lose_con < 10:
        for x in word:
            if x == i:
                win_con -= 1
                break
        else:
            lose_con += 1
    else:
        if win_con <= 0:
            print("WIN")
            break
        else:
            print("LOSE")
            break
