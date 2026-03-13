class Solution:
    def decodeString(self, s: str) -> str:
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
                while stack and stack[-1].isdigit():
                    numArr.append(stack.pop())
                numArr.reverse()
                num = "".join(numArr)
                num = int(num)
                temp = num * temp[::-1]
                stack.append("".join(temp))

        return "".join(stack)


