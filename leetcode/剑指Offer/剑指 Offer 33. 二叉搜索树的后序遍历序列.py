from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        root = postorder[-1]
        left_index = 0
        while postorder[left_index] < root:
            left_index += 1

        left = self.verifyPostorder(postorder[:left_index])

        if not left:
            return False

        right_array = postorder[left_index:len(postorder) - 1]
        for right_item in right_array:
            if right_item < root:
                return False

        right = self.verifyPostorder(right_array)

        return right
