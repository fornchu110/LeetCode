#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
# 找出給定矩陣grid中每3x3的子矩陣裡最大值並return

# By traversal(simulation), time: O(n^2), space: O(1)
# 善用列表生成式
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n =  len(grid)
        # 先生成n-2個0的一維陣列, 再將這個陣列生成n-2次
        # [0]*(n-2)也是生成一維陣列的作法, 但二維一定要用for
        res = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                # 利用列表生成式來從座標[i][j]開始做3*3的走訪並找出max設定成res[i][j]
                res[i][j] = max(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))
        return res

# @lc code=end

