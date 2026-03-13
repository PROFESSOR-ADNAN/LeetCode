class Solution:
    def decodeString(self, s: str) -> str:
    
        def isLetterOrBracket(ch):
            if len(ch) > 1: return True
            return (ord("a") <= ord(ch) <= ord('z')) or (ch == "[") or (ch == "]")

        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp = []
                while stack[-1] != "[":
                    top = stack.pop()
                    temp.append(top)
                stack.pop()
                numArr = []
                while stack and  not isLetterOrBracket(stack[-1]):
                    numArr.append(stack.pop())
                numArr.reverse()
                num = "".join(numArr)
                num = int(num)
                temp = num * temp[::-1]
                stack.append("".join(temp))

        return "".join(stack)


