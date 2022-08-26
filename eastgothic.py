goth_word = 0

inp = input().split(" ")

for i in inp:
    if "ae" in i:
        goth_word += 1

if goth_word/len(inp) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
