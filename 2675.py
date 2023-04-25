#2675

n = int(input())
s = []
for i in range(n):
    s.append(input().split())
for i in range(len(s)):
    str_split = list(s[i][1])
    for j in str_split:
        print(j*int(s[i][0]),end='')
    print()
