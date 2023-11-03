#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
# By min()、max() and index array, time: O(n^2), space: O(n)
# 因這題給方形所以O(n^2)
# 給多個建築物高度, 要在不影響東西南北看過去天際線情況下增加建築物高度
# 也就是說對每個建築物, 找出同row最高和同column最高, 增加至較小的那邊高度即可
# 不找較大那個是因為選較大的就會超出天際線, 較小才不會改變
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # row長度和col長度, 實際上這題因給方形建築分布所以m=n
        m = len(grid)
        n = len(grid[0])
        rowmax = list()
        colmax = list()
        res = 0
        # 用來確認增加高度後的grid用的, 實際上不需要
        # gridnew=[[0]*n for i in range(m)]
        # 找出每row最大值
        for i in grid:
            rowmax.append(max(i))
        # 找出每col最大值, 注意是col在外層, 因有n個col最大值
        for j in range(n):
            tmpmax = 0
            for i in grid:
                if i[j]>tmpmax:
                    tmpmax = i[j]
            colmax.append(tmpmax)
        # 對grid內每個建築物, 找出他所在row, col最大值中較小的那個
        for i in range(m):
            for j in range(n):
                # 確認用
                # gridnew[i][j] = min(rowmax[i], colmax[j])
                res += min(rowmax[i], colmax[j])-grid[i][j]
        return res

# 官方做法, 一樣意思但簡潔很多, 速度比較快
# By map() and zip(), time: O(n^2), space: O(n)
# 學會max()映射和zip(*list)將陣列轉置的作法
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         # map()是將陣列內元素做指定函數, map(max, grid)就是對grid內所有元素做max()
#         # 不會返回陣列, 要用list()將變換完的內容轉換成陣列
#         # 這邊這樣就等同找出每row最大值
#         rowMax = list(map(max, grid))
#         # zip(*grid)的作法想成轉置矩陣, 將行列互換, 這樣再做map()便是找每col最大值
#         # list(zip(grid))會在grid外再包一層
#         colMax = list(map(max, zip(*grid)))
#         return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))

# @lc code=end

