from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        key1 = counter1.keys()
        key2 = counter2.keys()
        if len(key1) != len(key2):
            return False
        for item in key1:
            if item not in key2:
                return False

        values1 = list(counter1.values())
        values2 = list(counter2.values())

        if len(values1) != len(values2):
            return False

        values1.sort()
        values2.sort()
        for i in range(len(values1)):
            if values1[i] != values2[i]:
                return False
        return True

if __name__ == '__main__':
    print(Solution().closeStrings('a', 'b'))
