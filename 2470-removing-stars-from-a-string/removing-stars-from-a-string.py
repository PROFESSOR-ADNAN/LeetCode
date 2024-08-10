class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for itm in s:
            if itm == "*":
                stack.pop()
            else:
                stack.append(itm)
        s = ""
        for elem in stack:
            s += elem
        return s