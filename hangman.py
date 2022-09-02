word = set(input())
inp = input()
lose = True
win_con = len(word)
lose_con = 10
inp_length = len(inp)
current_position = 0

while lose and inp_length > current_position and lose_con:
    if not win_con:
        lose = False
    if inp[current_position] in word:
        win_con -= 1
    else:
        lose_con -= 1
    current_position += 1
else:
    if lose:
        print("LOSE")
    else:
        print("WIN")
