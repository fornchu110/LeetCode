#
# @lc app=leetcode id=1476 lang=python3
#
# [1476] Subrectangle Queries
#

# @lc code=start

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle
        self.update = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        res = None
        for i in range(len(self.update)-1, -1, -1):
            row1,col1,row2,col2, val = self.update[i]
            if row1 <= row <= row2 and col1<= col <= col2:
                res = val
                break
        
        return res if res else self.data[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end

