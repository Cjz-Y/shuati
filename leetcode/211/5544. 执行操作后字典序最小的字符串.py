class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        def first_process(ss):
            templ = list(ss)
            for j in range(1, len(templ), 2):
                temp = int(templ[j]) + a
                temp %= 10
                templ[j] = str(temp)
            return ''.join(templ)

        def second_process(ss):
            return ss[len(ss) - b:] + ss[:len(ss) - b]

        ans = s
        use = set()

        cur = [s]
        while cur:
            next = []

            for current in cur:


                first = first_process(current)
                if first not in use:
                    next.append(first)
                    use.add(first)
                    ans = min(ans, first)

                second = second_process(current)
                if second not in use:
                    next.append(second)
                    use.add(second)
                    ans = min(ans, second)
            cur = next
        return ans
