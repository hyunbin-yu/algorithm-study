#2577

a = int(input())
b = int(input())
c = int(input())

abc = a*b*c
cnt = [0,0,0,0,0,0,0,0,0,0]

for i in str(abc):
    cnt[int(i)] += 1
for i in range(10):
    print(cnt[i])