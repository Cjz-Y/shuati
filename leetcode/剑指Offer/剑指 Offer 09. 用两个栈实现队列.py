class CQueue:

    def __init__(self):
        self.pushIn = []
        self.popOut = []


    def appendTail(self, value: int) -> None:
        self.pushIn.append(value)


    def deleteHead(self) -> int:
        if not self.popOut:
            if not self.pushIn:
                return -1
            else:
                while self.pushIn:
                    self.popOut.append(self.pushIn.pop())

        return self.popOut.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()