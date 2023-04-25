#10952

sum = []
while 1:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        sum.append(a+b)
    else:
        break

for i in sum:
    print(i)