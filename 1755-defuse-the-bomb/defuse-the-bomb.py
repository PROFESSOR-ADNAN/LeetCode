class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            l = 1
            r = l + k
            defused = sum(code[l:r])
            res = []
            res.append(defused)
            print("before: ", res)
            while l < len(code):
                if r >= len(code):
                    r = 0
                defused += (code[r]-code[l])
                print(l, r)
                print(defused)
                l += 1
                r += 1
                res.append(defused)
                print(res)

            return res
        else:
            l = len(code) + k
            r = l-k
            defused = sum(code[l:r])
            res = []
            res.append(defused)
            print("b: ", res)
            r = 0
            while r < len(code)-1:
                if l == len(code):
                    l = 0
                print(l, r)
                defused += (code[r]-code[l])
                print(defused)
                l += 1
                r += 1
                res.append(defused)
                print(res)

            return res