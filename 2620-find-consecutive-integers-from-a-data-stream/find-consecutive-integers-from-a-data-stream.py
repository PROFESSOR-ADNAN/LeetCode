class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.stream = deque()
        self.count = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if len(self.stream) == self.k:
            if self.stream[0] == self.value:
                self.count -= 1
            self.stream.popleft()
        self.stream.append(num)

        if num == self.value:
            self.count += 1

        return self.count == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

# class DataStream(object):

#     def __init__(self, value, k):
#         """
#         :type value: int
#         :type k: int
#         """
#         self.value = value
#         self.k = k
#         self.count = 0

#     def consec(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num == self.value:
#             self.count += 1
#         else:
#             self.count = 0
        
#         return self.count >= self.k

# # Your DataStream object will be instantiated and called as such:
# # obj = DataStream(value, k)
# # param_1 = obj.consec(num)

# class DataStream(object):

#     def __init__(self, value, k):
#         """
#         :type value: int
#         :type k: int
#         """
#         self.stream = deque()
#         self.value = value
#         self.k = k

#     def consec(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         self.stream.append(num)
#         if self.stream and len(self.stream) > self.k:
#             self.stream.popleft()     
#         for i in range(len(self.stream)):
#             if self.stream[i] != self.value:
#                 return False
#         return True if len(self.stream) == self.k else False



# # Your DataStream object will be instantiated and called as such:
# # obj = DataStream(value, k)
# # param_1 = obj.consec(num)