class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack = []
        # score = 0

        # for ch in s:
        #     if ch == "(":
        #         stack.append(ch)
        #     else:
        #         stack.pop()
        #         score += 1
        
        # return score

        # stack = []

        # for ch in s:
        #     if ch == "(":
        #         stack.append(ch)
        #     elif stack[-1] == "(":
        #         stack.pop()
        #         stack.append(1)
        #     else:
        #         curr = 0
        #         while stack and stack[-1] != "(":
        #             curr += stack.pop()
        #         stack.pop()
        #         stack.append(2*curr)

        # return sum(stack)

        stack = []
        score = 0

        for ch in s:
            if ch == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score, 1)

        return score
