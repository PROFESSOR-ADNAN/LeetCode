class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.size:
            self.q.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.size:
            self.q.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.q) > 0:
            self.q.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.q) > 0:
            self.q.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return False if self.q else True

    def isFull(self) -> bool:
        if len(self.q) == self.size:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()