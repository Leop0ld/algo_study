
def get_score(string):
    total_score = 0
    score = 1
    for i in string:
        if i == 'O':
            total_score += score
            score += 1
        else:
            score = 1

    print(total_score)

n = int(input())
input_str = []

for i in range(n):
    input_str.append(input())

for string in input_str:
    get_score(string)
