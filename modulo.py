inp = []
ans = 0
checkd_ans = []

for i in range(10):
    inp.append(int(input()))

for i in inp:
    modu = i % 42
    if modu in checkd_ans:
        continue
    else:
        checkd_ans.append(modu)
        ans += 1

print(ans)
