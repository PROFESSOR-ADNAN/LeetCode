# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:

#         def end_of_comment(i, j):
#             while j <= len(source[i]):
#                 if j == len(source[i]):
#                     j = 0
#                     i += 1
#                     continue
#                 if source[i][j] == "*":
#                     if j+1 < len(source[i]) and source[i][j+1] == "/":
#                         j += 1
#                         return
#                 j += 1

#         ans = []
#         i = 0
#         while i < len(source):
#             code = ""

#             j = 0
#             while j < len(source[i]):
#                 ch = source[i][j]
#                 block_comment = False
                
#                 if ch == "/":
#                     if j+1 < len(source[i]):
#                         if source[i][j+1] == "/":
#                             break
#                         if source[i][j+1] == "*":
#                             j += 2
#                             end_of_comment(i, j)
#                             block_comment = True

#                 if not block_comment:
#                     code += ch
#                 j += 1

#             if code: ans.append(code)
#             i += 1


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        curr_block = False
        curr_line = []
        code = []

        for line in source:

            if not curr_block:
                curr_line = []

            i = 0
            while i < len(line):
                if not curr_block and i+1 < len(line) and line[i:i+2] == "/*":
                    curr_block = True
                    i += 2
                elif curr_block and i+1 < len(line) and line[i:i+2] == "*/":
                    curr_block = False
                    i += 2
                elif not curr_block and i+1 < len(line) and line[i:i+2] == "//":
                    break
                elif not curr_block:
                    curr_line.append(line[i])
                    i += 1
                else:
                    i += 1

            if not curr_block and curr_line:
                code.append(''.join(curr_line))

        return code
