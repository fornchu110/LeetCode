# @lc code=start
# 給一二維陣列grid, grid[0]裡面有n個元素, grid[0][1] = 1代表第0個隊伍贏過第一個隊伍
# return 贏過所有隊伍的冠軍

# By simmulation, time: O(n^2), space: O(1)
# 直接for迴圈找出i!=j時grid[i][j]皆為1的隊伍
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        team_num = len(grid[0])
        for i in range(n):
            flag = 1
            for j in range(team_num):
                if i!=j and grid[i][j]==0:
                    flag = 0
            if flag:
                return i
                    
# @lc code=end