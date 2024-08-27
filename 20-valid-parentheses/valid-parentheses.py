class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mpp = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c in mpp:
                if stack and stack[-1] == mpp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

            




        # order = {")":"(", "}":"{", "]":"["}
        # stack = []
        # for itm in s:
        #     if itm not in order:
        #         stack.append(itm)
        #     elif stack[-1] == order[itm]:
        #         stack.pop()
        #     else:
        #         return False

        # return True if len(s) > 1 else False
     
        