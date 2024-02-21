people = 4
scores = []

bronze_score = 0

for i in range(0, people):
    new_score = int(input())
    scores.append(new_score)

def check_num():
    bigger_nums = []
    for i in range(0,people):
        for x in range(1,people-1):  
            if scores[i] < scores[i+x]: ## list index out of range,  was removed for testing--> "and scores[i+x] not in bigger_nums"
                bigger_nums.append(scores[i+x])

        if len(bigger_nums) == 2:
            bronze_score += scores[i]
            return print(bronze_score)
        elif len(bigger_nums) > 2 or len(bigger_nums) < 2:
            bigger_nums.clear()

check_num()
           

