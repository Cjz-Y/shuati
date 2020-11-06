import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 小根堆，存储较大一半的数
        self.high = []
        # 大根堆，存储较小一半的数
        self.low = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1

        if self.high:
            a = self.high[0]
        else:
            a = None

        if a and num > a:
            heapq.heappush(self.high, num)
        else:
            heapq.heappush(self.low, -num)

        if len(self.low) - len(self.high) == 2:
            item = -heapq.heappop(self.low)
            heapq.heappush(self.high, item)

        if len(self.high) - len(self.low) == 2:
            item = heapq.heappop(self.high)
            heapq.heappush(self.low, -item)


    def findMedian(self) -> float:
        if self.length % 2 == 0:
            a = self.high[0]
            b = -self.low[0]
            return (a + b) / 2
        else:
            return -self.low[0] if len(self.low) > len(self.high) else self.high[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()