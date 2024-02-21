dusa = int(input())
yubas_line = []

for i in range(0,6):
    new_yubas = input()
    if new_yubas == '':
        new_yubas = 0
    yubas_line.append(int(new_yubas))

for i in yubas_line:
    if dusa > i:
        dusa += i
    elif dusa <= i:
        break

print(dusa)
