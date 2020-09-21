from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        class TrieNode:
            def __init__(self, char):
                self.char = char
                self.time = 1
                self.map = {}

        def insert(s):
            index = 0
            temp = root
            while index < len(s):
                next = temp.map.get(s[index], None)
                if next:
                    next.time += 1
                else:
                    next = TrieNode(s[index])
                    temp.map[s[index]] = next

                temp = next
                index += 1


        n = len(strs)

        root = TrieNode('')

        for s in strs:
            insert(s)

        ans = ''

        while True:
            ans += root.char
            next = None

            for key, value in root.map.items():
                if value.time == n:
                    next = value
                    break

            if not next:
                break
            else:
                root = next
        return ans


