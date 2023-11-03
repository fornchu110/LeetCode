#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start

# By for traversal
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            # ��i�檺[0]~[n-2]�|�����i+1�檺[1]~[n-1]
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

# @lc code=end

