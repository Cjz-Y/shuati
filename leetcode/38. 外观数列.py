class Solution:
    def countAndSay(self, n: int) -> str:
        current = '1'
        for i in range(n - 1):
            index = 0
            next = ''
            while index < len(current):
                mark = current[index]
                mark_time = 0
                while index < len(current) and current[index] == mark:
                    mark_time += 1
                    index += 1
                next += str(mark_time) + mark

            current = next
        return current

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(5))
