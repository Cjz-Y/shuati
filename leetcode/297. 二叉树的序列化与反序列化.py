from leetcode.TreeNode import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        cur = [root]
        has_next = True
        ans = []
        while cur and has_next:
            has_next = False
            next = []
            for node in cur:
                if node:
                    ans.append(node.val)
                    if node.left or node.right:
                        has_next = True
                    next.append(node.left)
                    next.append(node.right)
                else:
                    ans.append(None)
                    next.append(None)
                    next.append(None)
            cur = next
        return str(ans)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        1,2,3
        1,2,3
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data) - 1]
        nodes = []
        nums = data.split(',')
        for i in range(len(nums)):
            temp = nums[i].strip()
            if temp != 'None':
                node = TreeNode(int(temp))
                father_index = int((i + 1) / 2) - 1
                if father_index != -1:
                    if (i + 1) % 2 == 0:
                        nodes[father_index].left = node
                    else:
                        nodes[father_index].right = node
                nodes.append(node)
            else:
                nodes.append(None)
        return nodes[0]


