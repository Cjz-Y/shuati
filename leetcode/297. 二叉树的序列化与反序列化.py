class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        cur = [root]
        ans = []
        while cur:
            for node in cur:
                if node:
                    ans.append(node.val)
                else:
                    ans.append(None)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

