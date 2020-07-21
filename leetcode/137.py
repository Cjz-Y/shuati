from typing import List

# ### 前提知识
# 0 ^ x = x
# x ^ x = 0
#
# 0 & x = 0
# 1 & x = x
#
# ### 本题思路
# 出现一次的存放在first中，第二次出现的时候，移除first，在second中存放，出现第三次则first不变，second中移除
# 为什么？
# 1. 因为位运算满足交换律，所以在这个过程中，无论与其他的数发生什么样的运算，都可以通过交换位置，把同样的数字理解到同一次的处理过程中
# 2. 异或0等于本身，本身异或等于0，基于此可以用来判断一个数字同时出现两次，但是需要判断三次就需要辅助变量来进行判断转移
#
# ### 本题公式
# ones = ones ^ num & ~twos
# 1. 进入第一个数
# ```
# ones = 0，ones ^ num = num
# twos = 0，~twos = 1
# ones = num
# ```
# 2. 进入第二个相同的数，把进入一次的数移走
# ```
# ones = num, ones ^ num = num ^ num = 0
# twos = 0, ~twos = 1
# ones = 0 & 1 = 0
# ```
# 3. 第三次出现数字
# ```
# ones = 0, ones ^ num = num
# twos = num, ~twos = ~num
# ones = num & ~num = 0
# ```
#
# twos = twos ^ num & ~ones
# 1. 进入第一个数
# ```
# twos = 0, twos ^ num = num
# ones = num, ~ones = ~num
# twos = num & ~num = 0
# ```
# 2. 进入第二个相同的数
# ```
# twos = 0, twos ^ num = num
# ones = 0, ~ones = 1
# twos = num & 1 = num
# ```
# 3. 第三次出现相同的数字
# ```
# twos = num, twos ^ num = num ^ num = 0
# ones = 0, ~ones = 1
# twos = 0 & 1 = 0
# ```

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first, second = 0, 0
        for num in nums:
            first = first ^ num & ~second
            second = second ^ num & ~first
        return first