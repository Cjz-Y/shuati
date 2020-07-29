from typing import List


class Solution:
    p = []
    ans = []

    def back(self, cur, result, s):
        if cur == len(s):
            self.ans.append(result.copy())
            return
        for i in range(len(self.p[cur])):
            temp = s[cur:self.p[cur][i] + 1]
            result.append(temp)
            self.back(self.p[cur][i] + 1, result, s)
            result.pop()



    def partition(self, s: str) -> List[List[str]]:
        # 初始化
        self.ans = []

        # 预处理
        # f[i,j]表示从i到j是否是回文串
        f = [[False] * len(s) for i in range(len(s))]

        # self.p[i]代表着从第i个位置起，后面有多少个位置跟i是回文串 "aab" self.p[0] = [0, 1]
        self.p = [[] for i in range(len(s))]

        # 每个字母自己必然是回文串
        for i in range(len(s)):
            f[i][i] = True
            self.p[i].append(i)

        # 两个相邻字母相等必然是回文串
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                f[i - 1][i] = True
                self.p[i - 1].append(i)

        # 当前是回文串，且两边的字母相等，则加上两边的也是回文串
        for length in range(1, len(s)):
            for start in range(0, len(s) - length + 1):
                end = start + length - 1
                if f[start][end] and start - 1 >= 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
                    f[start - 1][end + 1] = True
                    self.p[start - 1].append(end + 1)

        # for i in range(len(s)):
        #     print(self.p[i])

        self.back(0, [], s)
        return self.ans






