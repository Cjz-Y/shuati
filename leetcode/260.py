from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 对有所的数进行异或操作，出现两次的会在操作过程中得到0，最后的结果就是a^b的结果
        x = 0
        for num in nums:
            x ^= num

        # x = a ^ b, -x = ~x + 1, diff即为x二进制中最右边的那个1，意味着a和b在在这个1所在的位置不同
        # 通过这个不同可以将a和b分开，一个是二进制在这个位置=0，一个是在二进制在这个位置=1，这就是a和b的区别
        diff = x & -x

        # 通过利用a和b的区别，将整个数组分为两个组，其中a和b分别位于两组中，这两组分别包含若干个出现两次的和一个出现一次a或者b，然后利用之前的异或算法得到a或者b
        y = 0
        for num in nums:
            # 因为diff是一个其他位都为0，在不同的位置上是1的二进制，所以如果num在该位置上是1那么得到一个非零数，如果num在该位置上0，那么得到0，如此对数组进行分组
            if diff & num:
                y ^= num

        return [y, x ^ y]