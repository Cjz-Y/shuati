class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map = {}
        start = 0
        ans = 0

        for i in range(len(s)):
            pos = map.get(s[i], -1)
            if pos == -1 or pos < start:
                ans = max(ans, i - start + 1)
            else:
                start = pos + 1
            map[s[i]] = i

        return ans
