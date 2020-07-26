from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False for i in range(len(s))]
        for i in range(len(s)):
            for j in range(len(wordDict)):
                if i - len(wordDict[j]) == -1 or f[i - len(wordDict[j])]:
                    # print('i-len+1 = %d, i+1 = %d, s = %s' % (i - len(wordDict[j]) + 1, i + 1, s[i - len(wordDict[j]) + 1: i + 1]))
                    if s[i - len(wordDict[j]) + 1: i + 1] == wordDict[j]:
                        f[i] = True

                # print('i = %d, j = %d, f[i] = %s' % (i, j, f[i]))
                if f[i]:
                    break

        return f[len(s) - 1]


if __name__ == '__main__':
    s = Solution()
    wordDict = ['leet', 'code']
    print(s.wordBreak('leetcode', wordDict))