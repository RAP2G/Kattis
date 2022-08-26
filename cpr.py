inp = list(input().replace("-", ""))

if(int(inp[0])*4+int(inp[1])*3+int(inp[2])*2+int(inp[3])*7+int(inp[4])*6+int(inp[5])*5+int(inp[6])*4+int(inp[7])*3+int(inp[8])*2+int(inp[9])) % 11:
    print(0)
else:
    print(1)
