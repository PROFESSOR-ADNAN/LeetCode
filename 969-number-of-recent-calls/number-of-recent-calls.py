class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while t - self.queue[0] > 3000:
            self.queue.pop(0)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# class RecentCounter(object):

#     def __init__(self):
#         self.recent = deque()

#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """
#         while self.recent and t - self.recent[0] > 3000:
#                 self.recent.popleft()
#         self.recent.append(t)
#         return len(self.recent)


# # Your RecentCounter object will be instantiated and called as such:
# # obj = RecentCounter()
# # param_1 = obj.ping(t)