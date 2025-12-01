class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for s in s:
            if stack and s == "*":
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)
        

        # stack = []
        # for itm in s:
        #     if itm == "*":
        #         stack.pop()
        #     else:
        #         stack.append(itm)
        # s = ""
        # for elem in stack:
        #     s += elem
        # return s