red = int(input())
green = int(input())
blue = int(input())
total = 0

order = [red, green, blue]

for i in range(0,3):
    if i == 0:
        total += order[i]*3
    if i == 1:
        total += order[i]*4
    if i == 2: 
        total += order[i]*5

print(total)