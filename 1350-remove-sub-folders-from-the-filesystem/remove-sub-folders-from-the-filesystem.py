class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        i = 0
        ans = []
        while i < len(folder):
            ans.append(folder[i])
            i += 1
            while i < len(folder) and folder[i].startswith(ans[-1] + "/"):
                i += 1
        return ans

        