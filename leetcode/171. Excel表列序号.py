class Solution:
    def titleToNumber(self, s: str) -> int:
        temp = 1
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            num = ord(s[i]) - ord('A') + 1
            ans = num * temp
            temp *= 26

        return ans