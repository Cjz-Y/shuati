class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_pop = []
        self.stack_push = []
        self.front = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack_push) == 0:
            self.front = x
        self.stack_push.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack_pop) == 0:
            while len(self.stack_push) != 0:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack_pop) != 0:
            return self.stack_pop[len(self.stack_pop) - 1]
        else:
            return self.front


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_pop) == 0 and len(self.stack_push) == 0
