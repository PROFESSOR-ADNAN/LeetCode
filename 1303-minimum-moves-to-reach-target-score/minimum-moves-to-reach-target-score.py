class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while target > 1 and maxDoubles > 0:
            if target % 2:
                steps += 1
                target -= 1
            
            target //= 2
            steps += 1
            maxDoubles -= 1
        
        steps += target-1
        return steps
