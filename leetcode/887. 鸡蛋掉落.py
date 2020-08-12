class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        f = [[99999] * (N + 1) for i in range(K + 1)]

        # 0层楼的时候都是0次
        # 1层楼的时候都是1次
        for i in range(K + 1):
            f[i][0] = 0
            f[i][1] = 1

        # 1个鸡蛋的时候 所有的都是楼层数的次数
        # 0个鸡蛋的时候 都是0次
        for i in range(N + 1):
            f[0][i] = 0
            f[1][i] = i

        # 从2开始推算
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                left = 1
                right = j
                mid = 0
                while left < right:
                    mid = int((left + right) / 2)
                    # print('left = %d, mid = %d, right = %d' % (left, mid, right))
                    # print('t1 = f[%d][%d] = %d        t2 = f[%d][%d] = %d' % ((i - 1), (mid - 1), f[i - 1][mid - 1], i, (j - mid), f[i][j - mid]))
                    if left == mid:
                        break
                    if f[i - 1][mid - 1] > f[i][j - mid]:
                        right = mid
                    else:
                        left = mid

                f[i][j] = max(f[i - 1][mid - 1], f[i][j - mid]) + 1
                # print('mid = %d' % mid)
                # print('f[%d][%d] = %d' % (i, j, f[i][j]))
                # print()

        return f[K][N]

if __name__ == '__main__':
    s = Solution()
    print(s.superEggDrop(12, 8190))