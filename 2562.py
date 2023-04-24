#2562

num = []
for i in range(9):
    num.append(int(input()))
print(max(num))
for i in range(9):
    if max(num) == num[i]:
        print(i+1)