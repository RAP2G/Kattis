input()
inp = input().split()
ans = 0
for i in range(len(inp)):
    if i > 0:
        if int(inp[i]) <= int(inp[i-1]):
            continue
        else:
            ans += 1
    else:
        ans += 1

print(ans)
