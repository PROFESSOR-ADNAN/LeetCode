class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_map = {}
        splited_list = s.split(" ")
        ans = ""

        for word in splited_list:
            hash_map[int(word[-1])] = word[:-1:]
        for i in range(1, len(splited_list) + 1):
            ans += hash_map[i]
            if i != len(splited_list):
                ans += " "
        return ans