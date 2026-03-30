class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # if len(num) < 3: return False
        
        # seq = [num[0], num[1]]
        # for i in range(2, len(num)):
        #     seq.append(str(int(seq[i-1]) + int(seq[i-2])))

        # print(seq)
        # return num == "".join(seq)

        # if len(num) < 3: return False

        # ans = []
        # path = []

        # def backtrack(i):
        #     if i == len(num):
        #         # for k in range(2, len(path)):
        #         #     if int(path[k-1]) + int(path[k-2]) != int(path[k]):
        #         #         return False
        #         return len(path) >= 3

        #     for j in range(i, len(num)):
        #         val = num[i:j+1]
        #         if len(path) > 2 and int(val) != int(path[-1]) + int(path[-2]):
        #             continue
        #         if len(val) > 1 and int(val[0]) == 0:
        #             return

        #         path.append(val)
        #         if backtrack(j+1):
        #             if i == len(num):   
        #                 return True
        #         path.pop()

        #     return False

        # if backtrack(0): return True
        # else: return False

        if len(num) < 3: return False

        path = []

        def backtrack(i):
            if i == len(num):
                return len(path) >= 3

            for j in range(i, len(num)):
                val = num[i:j+1]
                
                if len(val) > 1 and int(val[0]) == 0:
                    return

                # if len(path) > 1:
                #     curr = int(val)
                #     prev = int(path[-1]) + int(path[-2])

                #     if curr > prev:
                #         break
                #     if curr < prev:
                #         continue

                if len(path) > 1 and int(val) != int(path[-1]) + int(path[-2]):
                    continue

                path.append(val)
                if backtrack(j+1):
                    return True
                path.pop()
        
        if backtrack(0): return True
        else: return False