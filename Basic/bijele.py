pieces = [1, 1, 2, 2, 2, 8]

inp = input().split(" ")
out = []

for i in range(6):
    out.append(str(pieces[i]-int(inp[i])))


print(' '.join(out))
