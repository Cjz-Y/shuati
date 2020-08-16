class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        ans = True
        while left <= right:
            while left < len(s) and not (s[left].isalpha() or s[left].isdecimal()):
                left += 1
            while right >= 0 and not (s[right].isalpha() or s[right].isdecimal()):
                right -= 1

            if left >= len(s) and right < 0:
                break

            # print('left = %s and right = %s' % (s[left], s[right]))
            if left < len(s) and right >= 0 and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                ans = False
                break
        return ans


if __name__ == '__main__':
    s = Solution()

    ss = "0P"
    print(s.isPalindrome(ss))