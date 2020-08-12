from typing import List


class Solution:

    class TreeNode:
        def __init__(self, val=None):
            self.val = val
            self.end = False
            self.father = None
            self.son = {}



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.tree
        for s in word:
            if s not in cur.son.keys():
                node = self.TreeNode(s)
                cur.son[s] = node
                node.father = cur
            cur = cur.son[s]
        cur.end = True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.tree
        for s in prefix:
            if s not in cur.son.keys():
                return False
            cur = cur.son[s]
        return True

    def dfs(self, x, y, node, use, board, result):
        next_xys = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]

        for next_x, next_y in next_xys:
            if (next_x, next_y) not in use and 0 <= next_x < len(board) and 0 <= next_y < len(board[x]) and board[next_x][next_y] in node.son.keys():
                use.add((next_x, next_y))
                self.dfs(next_x, next_y, node.son[board[next_x][next_y]], use, board, ''.join([result, board[next_x][next_y]]))
                use.remove((next_x, next_y))

        if node.end:
            # 添加答案
            self.ans.append(result)
            node.end = False

            # 删除已经找到的字符串
            if len(node.son) == 0:
                delete = node.father
                delete.son.pop(node.val)
                while len(delete.son) == 0 and not delete.end and delete.father:
                    father = delete.father
                    father.son.pop(delete.val)
                    delete = father




    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.tree = self.TreeNode('')
        for word in words:
            self.insert(word)

        self.ans = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.startsWith(board[i][j]):
                    use = set()
                    use.add((i, j))
                    self.dfs(i, j, self.tree.son[board[i][j]], use, board, board[i][j])

        return self.ans


if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    board = [["a", "a"]]
    words = ["aaa"]

    board = [["a", "b"], ["c", "d"]]
    words = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]

    solution = Solution()

    print(solution.findWords(board, words))