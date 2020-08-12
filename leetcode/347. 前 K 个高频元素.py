from typing import List


class Solution:

    def rejust(self, nums, times, target):
        """
        调整大根堆, 把一个小的丢到前面，然后往下沉
        :param nums:
        :param target:
        :return:
        """
        left = target * 2 + 1
        right = target * 2 + 2
        temp = target
        if left < len(nums) and times[left] > times[temp]:
            temp = left
        if right < len(nums) and times[right] > times[temp]:
            temp = right

        if temp != target:
            nums[temp], nums[target] = nums[target], nums[temp]
            times[temp], times[target] = times[target], times[temp]
            self.rejust(nums, times, temp)


    def insert(self, nums, times, pos, target):
        father = int((target + 1) / 2) - 1
        if father >= 0 and times[target] > times[father]:
            nums[target], nums[father] = nums[father], nums[target]
            times[target], times[father] = times[father], times[target]
            pos[nums[father]] = father
            pos[nums[target]] = target

            self.insert(nums, times, pos, father)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        times = []
        pos = {}

        for i in range(len(nums)):
            if nums[i] not in pos.keys():
                heap.append(nums[i])
                times.append(1)
                pos[nums[i]] = len(heap) - 1
                self.insert(heap, times, pos, len(heap) - 1)
            else:
                real_pos = pos[nums[i]]
                times[real_pos] += 1
                self.insert(heap, times, pos, real_pos)

        # print(heap)
        # print(times)

        ans = []
        for i in range(k):
            ans.append(heap[0])
            heap[len(heap) - 1], heap[0] = heap[0], heap[len(heap) - 1]
            times[len(times) - 1], times[0] = times[0], times[len(times) - 1]
            heap.pop()
            times.pop()
            self.rejust(heap, times, 0)

        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    solution = Solution()
    print(solution.topKFrequent(nums, k))