class Solution:

    def search(self, left, right):
        if left == right:
            if self.isBadVersion(left):
                return left
            else:
                return left + 1

        mid = int((left + right) / 2)
        if self.isBadVersion(mid):
            return self.search(left, mid)
        else:
            return self.search(mid + 1, right)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.search(1, n)



    def isBadVersion(self, version):
        pass