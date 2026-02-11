class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # if s == "codeleet":
        #     return "leetcode"

        # new_str = ""
        # for ind in indices:
        #     new_str += s[ind]

        # return new_str

        new_str = [""] * len(s)
        for k, ind in enumerate(indices):
            new_str[ind] = s[k]
        
        return "".join(new_str)
