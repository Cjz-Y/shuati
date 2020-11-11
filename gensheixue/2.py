import sys
n = int(sys.stdin.readline().strip())

matrix = [[] for i in range(n)]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    reverse_temp = []
    for j in range(n - 1, -1, -1):
        reverse_temp.append(temp[j])

    matrix[n - 1 - i] = reverse_temp

for i in range(n):
    a = str(matrix[i][0])
    for j in range(1, n):
        a = a + ' ' + str(matrix[i][j])
    print(a)
