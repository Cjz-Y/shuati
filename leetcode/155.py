class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.fmin = []
        self.head = -1


    def push(self, x: int) -> None:
        self.head = self.head + 1
        if self.head == len(self.stack):
            self.stack.append(x)
            if self.head == 0:
                self.fmin.append(x)
            else:
                self.fmin.append(min(self.fmin[self.head - 1], x))
        else:
            self.stack[self.head] = x

            if self.head == 0:
                self.fmin[self.head] = x
            else:
                self.fmin[self.head] = min(self.fmin[self.head - 1], x)




    def pop(self) -> None:
        self.head = self.head - 1


    def top(self) -> int:
        return self.stack[self.head]


    def getMin(self) -> int:
        return self.fmin[self.head]