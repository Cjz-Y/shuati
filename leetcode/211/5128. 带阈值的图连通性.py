from typing import List


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:

        def gcd(a, b):
            if a < b: a, b = b, a
            return a if b == 0 else gcd(b, a % b)

        def search(x):
            node = x
            while father[x] != x:
                father[x] = father[father[x]]
                x = father[x]
            father[node]= x
            return x

        father = [i for i in range(n + 1)]
        for i in range(threshold + 1, n + 1):
            for j in range(i + i, n + 1, i):

                father_one = search(i)
                father_two = search(j)
                if father_two != father_one:
                    father[father_two] = father_one


        ans = []
        for query in queries:
            x, y = query[0], query[1]
            father_x = search(x)
            father_y = search(y)
            if father_x != father_y:
                ans.append(False)
            else:
                ans.append(True)

        return ans



