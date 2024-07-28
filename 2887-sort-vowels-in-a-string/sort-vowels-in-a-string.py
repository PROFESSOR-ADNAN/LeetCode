class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ind = []
        vowels = []
        sett = ("a", "e", "i", "o", "u", "A", "E", "I","O", "U")
        str_to_list = []
        for itm in s:
            str_to_list.append(itm)
        for i in range(len(str_to_list)):
            if str_to_list[i] in sett:
                vowels.append([ord(str_to_list[i]), str_to_list[i]])
                ind.append(i)
        vowels.sort()
        for i in range(len(ind)):
            str_to_list[ind[i]] = vowels[i][1]
        final_str = ""
        for itm in str_to_list:
            final_str += itm
        return final_str
            