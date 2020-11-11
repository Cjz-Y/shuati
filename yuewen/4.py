import sys

n = int(sys.stdin.readline().strip())

matrix = []
for i in range(n):
    line = sys.stdin.readline().strip().split(',')
    matrix.append(line)


for i in range(n // 2):
    # 当前的start和end

    for j in range(i, n - i - 1):
        x, y = i, j
        temp = matrix[x][y]
        des_x = n - 1 - y
        des_y = x
        # print('(%d, %d) -> (%d, %d)' % (des_x, des_y, x, y))
        matrix[x][y] = matrix[des_x][des_y]
        x, y = des_x, des_y
        des_x = n - 1 - y
        des_y = x
        # print('(%d, %d) -> (%d, %d)' % (des_x, des_y, x, y))
        matrix[x][y] = matrix[des_x][des_y]
        x, y = des_x, des_y
        des_x = n - 1 - y
        des_y = x
        # print('(%d, %d) -> (%d, %d)' % (des_x, des_y, x, y))
        matrix[x][y] = matrix[des_x][des_y]
        matrix[des_x][des_y] = temp
ans = ''
for i in range(n):
    for j in range(n):
        ans += (matrix[i][j] + ',')
print(ans[:-1])






