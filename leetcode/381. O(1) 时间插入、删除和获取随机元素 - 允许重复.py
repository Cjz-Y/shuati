import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.arr = []



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        flag = val not in self.pos.keys() or len(self.pos[val]) == 0
        self.arr.append(val)
        pos_set = self.pos.get(val, set())
        pos_set.add(len(self.arr) - 1)
        self.pos[val] = pos_set
        return flag



    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.pos.keys() or len(self.pos[val]) == 0:
            return False

        pos_set = self.pos.get(val)
        # 如果就是最后加进来的，那么直接删掉就好
        if (len(self.arr) - 1) in pos_set:
            pos_set.remove(len(self.arr) - 1)
            self.arr.pop()
            self.pos[val] = pos_set
            return True

        value_pos = pos_set.pop()

        last_pos_value = self.arr[-1]
        last_pos__value_set = self.pos[last_pos_value]
        last_pos__value_set.add(value_pos)
        last_pos__value_set.remove(len(self.arr) - 1)
        self.pos[last_pos_value] = last_pos__value_set

        self.pos[val] = pos_set

        # print(len(self.arr), value_pos)/
        self.arr[value_pos], self.arr[-1] = self.arr[-1], self.arr[value_pos]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rand_int = random.randint(0, len(self.arr) - 1)
        return self.arr[rand_int]




# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()