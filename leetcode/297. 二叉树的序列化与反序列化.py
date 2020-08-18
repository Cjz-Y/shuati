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
                    next.append(node.left, node.right)
                else:
                    ans.append(None)
                    next.append(None, None)
            cur = next
        return str(ans)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data) - 1]
        nums = list(map(int, data.split(',')))

