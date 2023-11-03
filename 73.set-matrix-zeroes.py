<<<<<<< HEAD
#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# ���@��mxn��matrix, �p�Gmatrix����0, �h���0�Prow�Pcol���Ҧ��������ഫ��0

# By inplace flag array, time: O(m*n), space: O(1)
# �קK�F���B�~O(m+n)���Ŷ��x�sflag, �ӬO�Ѳ�0��row�M��0��col���x�s
# ���o�˷|����0��row�M��0��col������(���b�o�仪�����v�T, �󭫭n���O�i��|�|�F�N��0row�Bcol�������ഫ��0)
# �ҥH�n���P�_�̭��O�_�s�b0�å�flag����, �u�n�s�b0�N���row�Bcol���n�O0, �̫�A�N�������s��0�Y�i
# �Q���~��(��0row�Bcol)�M���骺0���ӴN�O���ۼv�T, �����u�n�b�Prow�Bcol��0, ��ӳ��n��0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # any()�O�P�_���󤺬O�_�s�b1��True, �u�n�s�b�Nreturn1, ���s�b�NFalse
        # �P�_��0��col�U���S����0������
        col0flag = any(matrix[i][0]==0 for i in range(m))
        # �P�_��0��row�U���S����0������
        row0flag = any(matrix[0][j]==0 for j in range(n))
        
        # �Hmatrix[i][0]�Mmatrix[0][j]�ӰO����i��row�H�β�j��col���S��0�s�b
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    #�o�ɰ��F�β�0row�Bcol�����~, �]���P����N��0row�Bcol�ഫ��0�F
                    matrix[i][0] = matrix[0][j] = 0
        
        # ���s���X��0��row�Bcol�~��matrix, �N��0��row�Mcol�Ҧ������ഫ��0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        # �p�Gcol0flag����0, �N���0��col�W���Prow���Ҧ����������ܬ�0
        if col0flag:
            for i in range(m):
                matrix[i][0] = 0
        # �p�Grow0flag����0, �N���0��row�W���Pcol���Ҧ����������ܬ�0
        if row0flag:
            for j in range(n):
                matrix[0][j] = 0

# By flag array, time: O(m*n), space: O(m+n)
# �o�D�n�`�N���O��ӳQ���ܦ�0���������Ӯ��ӳQ�P�_���Prow�Pcol��0, �p�G�Τ@�䨫�X�@��d��0���覡�N�|�����D
# Ex: ����matrix[3][2]�o�{�O0, ���W�U���k����אּ0, ������matrix[3][3]��, �o�����M�쥻�O1�Q��אּ0, ���|Ĳ�o�P�_��matrix[3][3]�W�U���k�אּ0
# �ҥH���[�����X�@��matrix, �N0�����Ҧb��row�Mcol�O���U��
# �A���X�@��matrix, �N�P�O���U��row�Mcol�Prow�Bcol��������אּ0
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         # 0�]�i�H��False�N��
#         rowflag = [0]*m
#         colflag = [0]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     # 0��False���ܳo��1�N�i�H���True
#                     rowflag[i] = 1
#                     colflag[j] = 1
#         for i in range(m):
#             for j in range(n):
#                 if rowflag[i] or colflag[j]:
#                     matrix[i][j] = 0

# @lc code=end

=======
#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# ���@��mxn��matrix, �p�Gmatrix����0, �h���0�Prow�Pcol���Ҧ��������ഫ��0

# By inplace flag array, time: O(m*n), space: O(1)
# �קK�F���B�~O(m+n)���Ŷ��x�sflag, �ӬO�Ѳ�0��row�M��0��col���x�s
# ���o�˷|����0��row�M��0��col������(���b�o�仪�����v�T, �󭫭n���O�i��|�|�F�N��0row�Bcol�������ഫ��0)
# �ҥH�n���P�_�̭��O�_�s�b0�å�flag����, �u�n�s�b0�N���row�Bcol���n�O0, �̫�A�N�������s��0�Y�i
# �Q���~��(��0row�Bcol)�M���骺0���ӴN�O���ۼv�T, �����u�n�b�Prow�Bcol��0, ��ӳ��n��0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # any()�O�P�_���󤺬O�_�s�b1��True, �u�n�s�b�Nreturn1, ���s�b�NFalse
        # �P�_��0��col�U���S����0������
        col0flag = any(matrix[i][0]==0 for i in range(m))
        # �P�_��0��row�U���S����0������
        row0flag = any(matrix[0][j]==0 for j in range(n))
        
        # �Hmatrix[i][0]�Mmatrix[0][j]�ӰO����i��row�H�β�j��col���S��0�s�b
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    #�o�ɰ��F�β�0row�Bcol�����~, �]���P����N��0row�Bcol�ഫ��0�F
                    matrix[i][0] = matrix[0][j] = 0
        
        # ���s���X��0��row�Bcol�~��matrix, �N��0��row�Mcol�Ҧ������ഫ��0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        # �p�Gcol0flag����0, �N���0��col�W���Prow���Ҧ����������ܬ�0
        if col0flag:
            for i in range(m):
                matrix[i][0] = 0
        # �p�Grow0flag����0, �N���0��row�W���Pcol���Ҧ����������ܬ�0
        if row0flag:
            for j in range(n):
                matrix[0][j] = 0

# By flag array, time: O(m*n), space: O(m+n)
# �o�D�n�`�N���O��ӳQ���ܦ�0���������Ӯ��ӳQ�P�_���Prow�Pcol��0, �p�G�Τ@�䨫�X�@��d��0���覡�N�|�����D
# Ex: ����matrix[3][2]�o�{�O0, ���W�U���k����אּ0, ������matrix[3][3]��, �o�����M�쥻�O1�Q��אּ0, ���|Ĳ�o�P�_��matrix[3][3]�W�U���k�אּ0
# �ҥH���[�����X�@��matrix, �N0�����Ҧb��row�Mcol�O���U��
# �A���X�@��matrix, �N�P�O���U��row�Mcol�Prow�Bcol��������אּ0
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         # 0�]�i�H��False�N��
#         rowflag = [0]*m
#         colflag = [0]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     # 0��False���ܳo��1�N�i�H���True
#                     rowflag[i] = 1
#                     colflag[j] = 1
#         for i in range(m):
#             for j in range(n):
#                 if rowflag[i] or colflag[j]:
#                     matrix[i][j] = 0

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
