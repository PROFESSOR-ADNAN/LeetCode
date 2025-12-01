class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapp = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket not in mapp:
                stack.append(bracket)
            else:
                if stack:
                    last_bracket_in_stack = stack.pop()
                    if mapp[bracket] != last_bracket_in_stack:
                        return False
                else:
                    return False
        return True if not stack else False
                

        # mpp = {")":"(", "}":"{", "]":"["}
        # stack = []
        # for c in s:
        #     if c in mpp:
        #         if stack and stack[-1] == mpp[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return True if not stack else False

            




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
     
        