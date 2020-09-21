class Solution:
    def replaceSpace(self, s: str) -> str:
        ss = list(s)

        for i in range(len(ss)):
            if ss[i] == ' ':
                ss[i] = '%20'

        return ''.join(ss)