#1157

n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0
for i in range(n):
    score[i] = score[i]/max_score * 100
    sum += score[i]
print(sum/n)