class Trie:
    class TreeNode:
        def __init__(self, val=None):
            self.val = val
            self.end = False
            self.son = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """

        node = self.TreeNode('')
        self.tree = node


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.tree
        for s in word:
            if s not in cur.son.keys():
                node = self.TreeNode(s)
                cur.son[s] = node
            cur = cur.son[s]
        cur.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.tree
        for s in word:
            if s not in cur.son.keys():
                return False
            cur = cur.son[s]
        return cur.end


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



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)