class DataStream:

    def __init__(self, value: int, k: int):
        # self.stream = []
        self.recent = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        # if num == self.value:
        #     self.stream.append(num)
        # else:
        #     self.stream.clear()

        # if len(self.stream) >= self.k: return True
        # else: return False

        if num == self.value: self.recent += 1
        else: self.recent = 0

        return self.recent >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)