import random
class Skiplist:

    class Node:
        def __init__(self, val, level):
            self.val = val
            self.level = level
            self.next = None
            self.down = None

    def __init__(self):

        self.max_level = 32
        self.p = 0.5

        self.heads = [self.Node(-1, i) for i in range(self.max_level)]

        for i in range(1, self.max_level):
            self.heads[i].down = self.heads[i - 1]

    def rand_level(self):
        level = 1
        while random.random() < self.p and level <= self.max_level:
            level += 1
        return level

    def search(self, target: int) -> bool:
        node = self.heads[-1]
        while True:
            while node.next and target >= node.next.val:
                node = node.next
            if node.level != 0:
                node = node.down
            else:
                break
        return node.val == target


    def add(self, num: int) -> None:
        spec_level = self.rand_level()
        level = spec_level - 1
        node = self.heads[level]

        up_node = None
        while True:
            while node.next and num >= node.next.val:
                node = node.next

            temp_node = self.Node(num, level)
            next_item = node.next
            node.next = temp_node
            temp_node.next = next_item

            if up_node:
                up_node.down = temp_node
            up_node = temp_node

            if node.level != 0:
                node = node.down
                level -= 1
            else:
                break



    def erase(self, num: int) -> bool:

        node = self.heads[-1]
        flag = False
        while True:
            while node.next and num > node.next.val:
                node = node.next
            if node.next and node.next.val == num:
                node.next = node.next.next
                flag = True

            if node.level != 0:
                node = node.down
            else:
                return flag




# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

if __name__ == '__main__':
    skiplist = Skiplist()

    # print(skiplist.add(1))
    # print(skiplist.add(2))
    # print(skiplist.add(3))
    # print(skiplist.search(0))
    # print(skiplist.add(4))
    # print(skiplist.search(1))
    # print(skiplist.erase(0))
    # print(skiplist.erase(1))
    # print(skiplist.search(1))

    # print(skiplist.add(0))
    # print(skiplist.add(5))
    # print(skiplist.add(2))
    # print(skiplist.add(1))
    # print(skiplist.search(0))
    # print(skiplist.erase(5))
    # print(skiplist.search(2))
    # print(skiplist.search(3))
    # print(skiplist.search(2))