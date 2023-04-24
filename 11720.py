n = int(input())
num = input()
numlist = list(num)
sum = 0
for i in range(n):
    sum += int(numlist[i])
print(sum)