class FrequencyTracker:

    def __init__(self):
        # self.frequency_tracker = []
        self.numberToFrequency = defaultdict(int)
        self.frequencyToCount = defaultdict(int)

    def add(self, number: int) -> None:
        # self.frequency_tracker.append(number)
        if number in self.numberToFrequency:
            self.frequencyToCount[self.numberToFrequency[number]] -= 1
            if self.frequencyToCount[self.numberToFrequency[number]] == 0:
                del self.frequencyToCount[self.numberToFrequency[number]]
        self.numberToFrequency[number] += 1
        self.frequencyToCount[self.numberToFrequency[number]] += 1

    def deleteOne(self, number: int) -> None:
        # if number in self.frequency_tracker:
        #     i = len(self.frequency_tracker) - 1
        #     while i >= 0 and self.frequency_tracker[i] != number:
        #         i -= 1
        #     self.frequency_tracker.pop(i)


        self.frequencyToCount[self.numberToFrequency[number]] -= 1
        if self.frequencyToCount[self.numberToFrequency[number]] <= 0:
                del self.frequencyToCount[self.numberToFrequency[number]]

        self.numberToFrequency[number] -= 1
        if self.numberToFrequency[number] == -1:
            del self.numberToFrequency[number]

        self.frequencyToCount[self.numberToFrequency[number]] += 1



    def hasFrequency(self, frequency: int) -> bool:
        # for number in self.frequency_tracker:
        #     if self.frequency_tracker.count(number) == frequency:
        #         return True
        
        # return False

        # for freq in self.numberToFrequency.values():
        #     if freq == frequency:
        #         return True

        # return False

        # return frequency in self.numberToFrequency.values()

        return frequency in self.frequencyToCount

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)