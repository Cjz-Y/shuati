class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map = {}
        start = 0
        end = 0
        ans = 1
        while end < len(s):
            pos = map.get(s[end], -1)
            if pos >= start:
                start = pos + 1
            map[s[end]] = end

            ans = max(ans, end - start + 1)
            end += 1

        return ans