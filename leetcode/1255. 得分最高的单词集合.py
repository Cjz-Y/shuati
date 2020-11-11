from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0

        use = Counter(letters)
        def search(index, total):
            nonlocal ans
            if total > ans:
                ans = total

            if index >= len(words):
                return

            can = True
            temp_counter = Counter(words)
            for key, value in temp_counter.items():
                can_use = use.get(key, 0)
                if can_use < value:
                    can = False
                    break

            if can:
                for key, value in temp_counter.items():
                    use[key] -= value
                    total += value * score[ord(key) - ord('a')]

                search(index + 1, total)

                for key, value in temp_counter.items():
                    use[key] += value
                    total -= value * score[ord(key) - ord('a')]

            search(index + 1, total)


        search(0, 0)

        return ans



