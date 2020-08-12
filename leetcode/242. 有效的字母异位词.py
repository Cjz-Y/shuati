class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = [0 for i in range(26)]
        tt = [0 for i in range(26)]
        for char in s:
            ss[ord(char) - ord('a')] += 1

        for char in t:
            tt[ord(char) - ord('a')] += 1

        for i in range(26):
            if ss[i] != tt[i]:
                return False
        return True