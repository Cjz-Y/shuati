#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回最大和的字符串
# @param x string字符串 即题目描述中所给字符串
# @param k int整型 即题目描述中所给的k
# @return string字符串
#
class Solution:
    def Maxsumforknumers(self , x , k ):
        # write code here
        arr = list(x)
        arr.sort(reverse=True)
        # print(arr)

        string = ''.join(arr)
        index = len(string) - k + 1
        ans = int(string[:index])
        for i in range(index, len(string)):
            ans += int(string[i])
        return ans

if __name__ == '__main__':
    print(Solution().Maxsumforknumers("345", 2))