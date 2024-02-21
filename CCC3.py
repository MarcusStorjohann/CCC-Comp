people = int(input())
scores = []

bronze_score = 0

for i in range(0, people):
    new_score = int(input())
    scores.append(new_score)

def check_num():
    global bronze_score
    bigger_nums = []
    for i in range(0,people):
        for x in range(1,people):  
            if scores[i] < scores[x]: 
                bigger_nums.append(scores[x])

        if len(bigger_nums) == 2:
            bronze_score += scores[i]
            return bronze_score
        elif len(bigger_nums) > 2 or len(bigger_nums) < 2:
            bigger_nums.clear()

check_num()
amount = 0
for i in scores:
    if i == bronze_score:
        amount +=1

print(str(bronze_score) + ' ' + str(amount))

