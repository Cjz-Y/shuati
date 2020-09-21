class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0 for i in range(len(num1) + len(num2) + 1)]
        n1 = len(num1)
        n2 = len(num2)

        for ii in range(n1 - 1, -1 , -1):
            i = 
            for jj in range(n2 - 1, -1, -1):
                target = i + j
                result[target] += num1
                result[target + 1] += int(result[target] / 10)