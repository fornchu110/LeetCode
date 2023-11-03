#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
# 給矩陣mat, 要求將矩陣位於兩條對角線的元素作加總, return加總值

# By math, time: O(n), space: O(1) 
# 要同時將兩條對角線元素做相加, 只走訪列而不用走訪矩陣所有元素省下複雜度
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n//2
        for i in range(n):
            # 第一行[0][0]對應[n-1][n-1], 第二行[1][1]對應[n-2][n-2], n-2等同n-1-1  
            total += mat[i][i] + mat[i][n-1-i]
        # len(mat)為奇數時最中間那格會被算兩次, 所以要扣回來
        return total-mat[mid][mid]*(n&1)

# By enumerate, time: O(n^2), space: O(1)
# 走訪矩陣所有元素, 當位於兩條對角線經過的座標就將其加總
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n = len(mat)
#         return sum(mat[i][j] for i in range(n) for j in range(n) \
#                     if i==j or i+j==n-1)

# @lc code=end

