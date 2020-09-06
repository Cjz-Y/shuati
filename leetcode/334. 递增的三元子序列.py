from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        heap = []
        for num in nums:
            if not heap:
                heap.append(num)
            else:
                if num > heap[-1]:
                    heap.append(num)
                else:
                    index = len(heap) - 1
                    while index >= 0 and heap[index] > num:
                        index -= 1
                    index += 1
                    heap[index] = num
            if len(heap) >= 3:
                return True
        return False

