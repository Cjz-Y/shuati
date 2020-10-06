class LRUCache:

    class LinkNode():
        def __init__(self, key):
            self.key = key
            self.next = None
            self.pre = None

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

        self.nodeMap = {}
        self.head = self.LinkNode(None)
        self.tail = self.LinkNode(None)
        self.head.next = self.tail
        self.tail.pre = self.head



    def get(self, key: int) -> int:
        temp = self.map.get(key, -1)
        if temp != -1:
            # 更新链表
            tempNode = self.nodeMap.get(key)

            # 提取node元素，缝合链表
            pre = tempNode.pre
            next = tempNode.next
            if pre:
                pre.next = next
                if next:
                    next.pre = pre

            # 将node放到head
            pre_head = self.head.next
            self.head.next = tempNode
            pre_head.pre = tempNode

            tempNode.pre = self.head
            tempNode.next = pre_head

        return temp

    def put(self, key: int, value: int) -> None:
        if key not in self.map.keys():
            if len(self.map) >= self.capacity:
                lastUseNode = self.tail.pre
                lastUseKey = lastUseNode.key

                # 在链表中删除
                lastLast = lastUseNode.pre
                lastLast.next = self.tail
                self.tail.pre = lastLast

                # 从两张表中删除
                self.map.pop(lastUseKey)
                self.nodeMap.pop(lastUseKey)

            node = self.LinkNode(key)
            self.nodeMap[key] = node

            firstUseNode = self.head.next
            firstUseNode.pre = node
            self.head.next = node

            node.pre = self.head
            node.next = firstUseNode
        else:
            self.get(key)

        a = []
        temp = self.head
        while temp:
            a.append(str(temp.key))
            temp = temp.next
        print('->'.join(a))

        self.map[key] = value





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)