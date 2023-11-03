#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
# 給一個二維陣列grid, 1是陸地0是海, return飛地(enclave)數量
# 飛地的定義: 無法經過任意次往其他陸地走而延伸到邊界的陸地數量

# 以後再寫
# By DFS, time: O(mn), space: O(mn)
# 島嶼問題都可以用DFS和BFS解
# 注意本來就在邊界的陸地一定不是飛地, 所以只要走訪最外圈以外的grid
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:
                return
            vis[r][c] = True
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(x, y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))
    
# @lc code=end

