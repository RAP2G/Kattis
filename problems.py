inp = input()
ans = [int(x) for x in inp]
temp = []
if len(ans) > 1:
    temp.append(ans.pop(-2))
if ans:
    temp.append(ans.pop(-1))
if ans:
    if int(''.join(str(e) for e in temp)) == 0:
        res = int(''.join(str(e) for e in ans))-1
        ans = []
        ans.append(res)
    elif int(''.join(str(e) for e in temp)) < 49:
        ans[-1] = ans[-1]-1

ans.append(9)
ans.append(9)
if int(''.join(str(e) for e in ans)) > 0:
    print(''.join(str(e) for e in ans))
else:
    print(99)
