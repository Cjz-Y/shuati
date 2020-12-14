class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n):
            unuse = n - i -1
            if unuse * 26 >= k:
                ans.append('a')
                k -= 1
            else:
                temp = k - unuse * 26
                ans.append(chr(ord('a') + temp - 1))
                k -= temp
        return ''.join(ans)