import math
# print(math.log2(3))

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param n long长整型 表示标准完全二叉树的结点个数
# @return long长整型
#
class Solution:
    def tree4(self , n ):
        # write code here
        mod = 998244353
        ans = 0

        index = 0
        while (1 << (index + 1)) < n:
            last = 1 << index
            current = (1 << (index + 1)) - 1
            sum = (last + current) * (current - last + 1) // 2

            # print(index, last, current, sum)
            ans = (ans + sum * (index + 1)) % mod
            index += 1
        last = 1 << index
        current = n
        sum = (last + current) * (current - last + 1) // 2
        ans = (ans + sum * (index + 1)) % mod




        # for i in range(1, n + 1):
        #     depth = (math.floor(math.log2(i)) + 1)
        #     print(i, depth)
        #     ans = (ans + i * depth) % mod

        return ans


# if __name__ == '__main__':
#     print(Solution().tree4(5))