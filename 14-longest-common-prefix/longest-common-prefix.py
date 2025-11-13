class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minL = float("inf")
        for st in strs:
            if len(st) < minL:
                minL = len(st)
        common_prefix_set = set()
        common_prefix = ""
        for i in range(minL):
            for st in strs:
                common_prefix_set.add(st[i])
            if len(common_prefix_set) > 1:
                break
            else:
                prefix = common_prefix_set.pop()
                common_prefix += prefix

        return common_prefix








        # minL = float('inf')
        # for s in strs:
        #     if len(s) < minL:
        #         minL = len(s)

        # prefix = ''
        # for i in range(minL):
        #     prefix += strs[0][i]
        #     for s in strs:
        #         if prefix[i] != s[i]:
        #             return prefix[:i]
        # return prefix
                
















        # commonPrefix = []

        # if strs == [""]:
        #     checker1 = ""
        # else:
        #     checker1 = strs[0][0]

        # print(checker1)
        # checker2 = ""
        # index = 0

        # length = 200

        # for str in strs:
        #     if len(str) < length:
        #         length = len(str)
        #         print(length)
        # print(length)

        # while index <= length - 1:
        #     for str in strs:
        #         checker2 = str[index]
        #         print(checker2)
        #         if checker2 != checker1:
        #             break
        #     if checker2 == checker1:
        #         commonPrefix.append(checker2)
        #         index += 1
        #         try:
        #             checker1 = strs[0][index]
        #         except IndexError:
        #             print("index out of range")
        #         print(index)
        #     else:
        #         break

        # longestCommonPrefix = ''.join(commonPrefix) 
        # return(longestCommonPrefix)