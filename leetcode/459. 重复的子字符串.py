class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


    def _repeatedSubstringPattern(self, s: str) -> bool:

        def gongyue(a, b):
            if b > a:
                a, b = b, a
            if b == 0:
                return a
            else:
                return gongyue(b, a % b)

        time = {}
        for i in range(len(s)):
            time[s[i]] = time.get(s[i], 0) + 1

        length = set()
        for key in time.keys():
            length.add(time[key])
        length = list(length)

        size = length[0]
        if len(length) != 1:
            index = 1
            while index < len(length):
                size = gongyue(size, size % length[index])
                index += 1

        if size == 1:
            return False

        # 这里需要枚举size的约数， 然后不断尝试

        skip = len(s) // size
        for i in range(len(s) - skip):
            if s[i] != s[i + skip]:
                return False

        return True


