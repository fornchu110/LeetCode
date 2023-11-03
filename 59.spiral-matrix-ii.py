#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0]*n for _ in range(n)]
        row, col, dir_idx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dir_idx]
            r, c = row+dx, col+dy
            if r<0 or r>=n or c<0 or c>=n or matrix[r][c]>0:
                dir_idx = (dir_idx+1)%4  
                dx, dy = dirs[dir_idx]
            row, col = row+dx, col+dy
        
        return matrix
    
# @lc code=end

