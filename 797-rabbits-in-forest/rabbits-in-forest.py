class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # answers.sort()
        # rabbits = 0
        # ind = 0
        # n = len(answers)
        # flag = 0
        # while ind < n:
        #     if answers[ind] != 1 and answers[ind] != 0 and ind > 0 and answers[ind] == answers[ind-1]:
        #         ind += 1
        #         continue

        #     if answers[ind] == 0:
        #         rabbits += 1
        #     elif answers[ind] == 1:
        #         flag += 1
        #         if flag % 2:
        #             rabbits += 2
        #     else:
        #         rabbits += 1 + answers[ind]
        #     ind += 1
        
        # return rabbits

        # n = len(answers)
        # flag = defaultdict(int)
        # count = defaultdict(int)
        # rabbits = 0

        # for val in answers:
        #     if val == 0:
        #         rabbits += 1
        #         continue

        #     flag[val] += 1
        #     count[val] += 1

        #     if count[val] > val+1:
        #         rabbits += 1 + val
        #     elif flag[val] % 2:
        #         rabbits += 1 + val

        # return rabbits

        # freq = defaultdict(int)
        # rabbits = 0

        # for val in answers:
        #     if val == 0:
        #         rabbits += 1
        #         continue

        #     freq[val] += 1
        #     if freq[val] == val + 1:
        #         rabbits += val + 1
        #         freq[val] = 0

        # for color, cnt in freq.items():
        #     if cnt > 0:
        #         rabbits += color + 1

        # return rabbits

        freq = defaultdict(int)
        count = 0
        for ans in answers:
            freq[ans] += 1
            if freq[ans] == ans + 1:
                count += ans + 1
                freq[ans] = 0

        for f, v in freq.items():
            if v > 0:
                count += f + 1

        return count


    












