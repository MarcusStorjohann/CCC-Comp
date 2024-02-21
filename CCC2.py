dusa = int(input())
yubas_line = []

for i in range(0,6):
    new_yubas = int(input())
    yubas_line.append(new_yubas)

for i in yubas_line:
    if dusa > i:
        dusa += i
    elif dusa <= i:
        break

print(dusa)
