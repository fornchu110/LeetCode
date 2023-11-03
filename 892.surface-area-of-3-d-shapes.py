<<<<<<< HEAD
#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans

# @lc code=end

=======
#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
