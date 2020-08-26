class Solution:
    def countSubstrings(self, s: str) -> int:
        t = ['#']
        for ss in s:
            t.append(ss)
            t.append('#')

        center, right, size = 1, 2,len(t)
        p = [0, 1] + [None] * (size - 2)

        ans = 0
        for i in range(2, size):
            mirror = center - (i - center)
            if i < right and p[mirror] < right - i:
                p[i] = p[mirror]
            else:
                count = min(i, size - i - 1)
                for length in range(1 if i > right else right - i + 1, count + 1):
                    if t[i + length] != t[i - length]:
                        count = length - 1
                        break

                center = i
                right = i + count
                p[i] = count
            ans += (p[i] + 1) // 2

        return ans

