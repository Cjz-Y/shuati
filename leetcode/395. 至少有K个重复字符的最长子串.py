class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def make(string):
            map = {}
            for c in string:
                map[c] = map.get(c, 0) + 1

            max_value = -1
            max_key = ''
            for key, value in map.items():
                if value < k and value > max_value:
                    max_value = value
                    max_key = key

            if max_value == -1:
                return len(string)
            else:
                l = string.split(max_key)
                max_value = 0
                for item in l:
                    if len(item) >= k:
                        max_value = max(max_value, make(item))

                return max_value

        return make(s)