<<<<<<< HEAD
#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
# ���x�}mat, �n�D�N�x�}������﨤�u�������@�[�`, return�[�`��

# By math, time: O(n), space: O(1) 
# �n�P�ɱN����﨤�u�������ۥ[, �u���X�C�Ӥ��Ψ��X�x�}�Ҧ������٤U������
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n//2
        for i in range(n):
            # �Ĥ@��[0][0]����[n-1][n-1], �ĤG��[1][1]����[n-2][n-2], n-2���Pn-1-1  
            total += mat[i][i] + mat[i][n-1-i]
        # len(mat)���_�Ʈɳ̤�������|�Q��⦸, �ҥH�n���^��
        return total-mat[mid][mid]*(n&1)

# By enumerate, time: O(n^2), space: O(1)
# ���X�x�}�Ҧ�����, �������﨤�u�g�L���y�дN�N��[�`
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n = len(mat)
#         return sum(mat[i][j] for i in range(n) for j in range(n) \
#                     if i==j or i+j==n-1)

# @lc code=end

=======
#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
# ���x�}mat, �n�D�N�x�}������﨤�u�������@�[�`, return�[�`��

# By math, time: O(n), space: O(1) 
# �n�P�ɱN����﨤�u�������ۥ[, �u���X�C�Ӥ��Ψ��X�x�}�Ҧ������٤U������
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n//2
        for i in range(n):
            # �Ĥ@��[0][0]����[n-1][n-1], �ĤG��[1][1]����[n-2][n-2], n-2���Pn-1-1  
            total += mat[i][i] + mat[i][n-1-i]
        # len(mat)���_�Ʈɳ̤�������|�Q��⦸, �ҥH�n���^��
        return total-mat[mid][mid]*(n&1)

# By enumerate, time: O(n^2), space: O(1)
# ���X�x�}�Ҧ�����, �������﨤�u�g�L���y�дN�N��[�`
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n = len(mat)
#         return sum(mat[i][j] for i in range(n) for j in range(n) \
#                     if i==j or i+j==n-1)

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
