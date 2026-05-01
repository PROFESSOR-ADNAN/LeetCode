"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        n = len(employees)
        
        def dfs(i):
            nonlocal sm
            
            sm += employees[i].importance
            for nei in employees[i].subordinates:
                dfs(posInList[nei])
        

        posInList = {}
        for i in range(n):
            currId = employees[i].id
            posInList[currId] = i

        sm = 0
        dfs(posInList[id])
        return sm
