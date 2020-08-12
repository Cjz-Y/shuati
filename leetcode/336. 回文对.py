from typing import List


class Solution:
    class TreeNode():
        def __init__(self, val):
            self.val = val
            self.son = {}
            self.end = False
            self.index = None


    def insert(self, words, index):
        cur = self.tree
        for word in words:
            if word not in cur.son.keys():
                node = self.TreeNode(word)
                cur.son[word] = node
            cur = cur.son[word]
        cur.end = True
        cur.index = index

    def search(self, word, reverse=True):
        if reverse:
            range_item = range(len(word) - 1, -1, -1)
        else:
            range_item = range(len(word))

        cur = self.tree
        for i in range_item:
            c = word[i]
            if c not in cur.son.keys():
                return -1
            cur = cur.son[c]
        if not cur.end:
            return -1
        else:
            return cur.index






    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.ans = []
        self.tree = self.TreeNode('')
        null = -1
        for i in range(len(words)):
            self.insert(words[i], i)
            if words[i] == '':
                null = i

        for i in range(len(words)):
            word = words[i]

            # print('word = %s' % (word))


            for start in range(len(word) - 1, 0, -1):
                flag = True
                little_word = word[start:len(word) + 1]
                for index in range(int((len(word) - start + 1) / 2)):
                    if little_word[index] != little_word[-index - 1]:
                        flag = False
                        break
                # 以end结尾的是回文串，搜搜end：结尾的反转在字典树中吗
                if flag:
                    # print('start = %d and word = %s' % (start, word[0:start]))
                    result = self.search(word[0:start], reverse=True)
                    if result != -1 and result != i:
                        self.ans.append([i, result])

            # print('start = %s' % self.ans)

            for end in range(len(word)):
                flag = True
                little_word = word[0:end + 1]
                for index in range(int((end + 1) / 2)):
                    if little_word[index] != little_word[-index - 1]:
                        flag = False
                        break
                # 以end结尾的是回文串，搜搜end：结尾的反转在字典树中吗
                if flag:
                    # print('end = %d' % end)
                    if end < len(word) - 1:
                        result = self.search(word[end + 1:len(word)])
                        if result != -1 and result != i:
                            self.ans.append([result, i])
                    if end == len(word) - 1 and null != -1:
                        self.ans.append([i, null])
                        self.ans.append([null, i])

            result = self.search(word)
            if result != -1 and result != i:
                self.ans.append([i, result])

            # print('end = %s' % self.ans)

        return self.ans


if __name__ == '__main__':
    a = ["abcd","dcba","lls","s","sssll"]
    a = ["a", "abc", "aba", ""]


    a = ["a", "b", "c", "ab", "ac", "aa"]


    a = ["ab", "ba", "abc", "cba"]

    solution = Solution()
    print(solution.palindromePairs(a))