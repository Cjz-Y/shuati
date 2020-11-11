import sys

m, p, n = map(int, sys.stdin.readline().strip().split(','))

a = []

for i in range(m):
    line = list(map(int, sys.stdin.readline().strip().split(',')))
    a.append(line)

b = []
for i in range(p):
    line = list(map(int, sys.stdin.readline().strip().split(',')))
    b.append(line)

ans = []
for i in range(m):
    line = []

    for j in range(n):
        temp = 0
        for k in range(p):
            temp += (a[i][k] * b[k][j])
        line.append(temp)
    ans.append(line)
print(ans)
