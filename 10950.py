#10950
sum_list = []
n = int(input())
for i in range(n):
    a, b = input().split()
    sum_list.append(int(a) + int(b))
for i in range(n):
    print(sum_list[i])