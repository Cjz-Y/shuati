from typing import List


class Solution:

    f = []
    ans = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        temp = set("".join(wordDict))
        if any([i not in temp for i in s]):
            return []
        f = []
        for i in range(len(s)):
            f.append([])
            for j in range(len(wordDict)):
                if i - len(wordDict[j]) == -1 and s[i - len(wordDict[j]) + 1:i+1] == wordDict[j]:
                    f[i].append(wordDict[j])
                elif i - len(wordDict[j]) >= 0 and len(f[i - len(wordDict[j])]) != 0 and s[i - len(wordDict[j]) + 1:i+1] == wordDict[j]:
                    for pre in f[i - len(wordDict[j])]:
                        f[i].append(pre + " " + wordDict[j])

            # print(f[i])
        return f[len(s) - 1]



    def back(self, s, cur, wordDict, result):
        print(result)
        if cur == len(s):
            # print('result = %s' % result.strip())
            self.ans.append(result.strip())
            return
        if cur > len(s):
            return
        for i in range(len(self.f[cur])):
            # print(wordDict[self.f[cur][i]])
            self.back(s, cur + len(wordDict[self.f[cur][i]]), wordDict, ' '.join([result, wordDict[self.f[cur][i]]]))


    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:

        self.f = []
        self.ans = []
        for i in range(len(s)):
            temp = []
            for j in range(len(wordDict)):
                if s[i:i+len(wordDict[j])] == wordDict[j]:
                    temp.append(j)
            self.f.append(temp)
            # print(temp)


        self.back(s, 0, wordDict, '')
        return self.ans





if __name__ == '__main__':
    s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    wordd = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # s = "catsanddog"
    # wordd = ["cat", "cats", "and", "sand", "dog"]

    solution = Solution()
    print(solution.wordBreak(s, wordd))



