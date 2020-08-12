class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = [int(x) for x in num1]
        nums1.reverse()

        nums2 = [int(x) for x in num2]
        nums2.reverse()

        length = max(len(nums1), len(nums2))

        result = [0 for i in range(length + 1)]
        for i in range(length):
            temp  = 0
            if i < len(nums1):
                temp += nums1[i]
            if i < len(nums2):
                temp += nums2[i]
            result[i + 1] = temp / 10
            result[i] = temp % 10

        result = reversed(result)
        result_str = [str(x) for x in result]
        return int(''.join(result_str))