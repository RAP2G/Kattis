inp = input()

s_count = 0

for i in inp:
    if i == "s":
        s_count += 1
    else:
        s_count = 0
    if s_count == 2:
        break

if s_count == 2:
    print("hiss")
else:
    print("no hiss")
