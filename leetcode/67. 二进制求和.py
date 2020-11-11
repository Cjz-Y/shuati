class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al = list(a)
        bl = list(b)

        def reverse(l):
            start = 0
            end = len(l) - 1
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1

        reverse(al)
        reverse(bl)

        c = []
        if len(al) < len(bl):
            al, bl = bl, al

        temp = 0
        for i in range(len(al)):
            index = int(al[i]) + temp
            if i < len(bl):
                index = index + int(bl[i])
            temp = index // 2
            index = index % 2
            c.append(index)
        if temp != 0:
            c.append(temp)

        reverse(c)

        return ''.join(list(map(int, c)))

