#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 求最小差值
# @param a int整型一维数组 数组a
# @return int整型
#
class Solution:
    def minDifference(self , a ):
        # write code here
        a.sort()
        ans = 99999999
        for i in range(1, len(a)):
            ans = min(ans, a[i] - a[i - 1])
        return ans