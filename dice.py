from math import floor
gun = input().split()
emm = input().split()
g1 = 0
g2 = 0
e1 = 0
e2 = 0
for i in range(int(gun[1])):
    g1 += (int(gun[0])+i)/int(gun[1])
for i in range(int(gun[3])):
    g2 += (int(gun[2])+i)/int(gun[3])
for i in range(int(emm[1])):
    e1 += (int(emm[0])+i)/int(emm[1])
for i in range(int(emm[3])):
    e2 += (int(emm[2])+i)/int(emm[3])

if round(g1+g2, ".4f") == (e1+e2):
    print("Tie")
elif g1+g2 > e1+e2:
    print("Gunnar")
elif g1+g2 < e1+e2:
    print("Emma")
