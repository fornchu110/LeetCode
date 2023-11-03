<<<<<<< HEAD
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
            # 第i行的[0]~[n-2]會等於第i+1行的[1]~[n-1]
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

# @lc code=end

=======
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
            # 第i行的[0]~[n-2]會等於第i+1行的[1]~[n-1]
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
