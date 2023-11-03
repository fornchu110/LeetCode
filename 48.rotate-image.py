#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
# ���@�G���}�Cmatrix, �n�D�Nmatrix��inplace����������90��, �ҥH����return

# By inplace modification, time: O(n^2), space: O(1)
# �������ϥ��B�~���Ŷ�(���U�x�})�ӰO��, ������inplace�վ�
# �N�@�Ӥ�������90�|�������m, ����180�B270�S���ӹ�����m, ����360�h�^����
# �ҥH��ڤW�L�׹�matrix�����󤸯�, ���O�b����P90�B180�B270�o�T��m�W���������ܧ�
# Ex �|���O1�B3�B9�B7, ��������90�ܦ�7�B1�B3�B9
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # �C4�Ӥ����|�O�@��, �ҥH�j���|��n^2/4, �]�N�O(n/2)*(n/2)��
        # �@���ư��k���U��
        for i in range(n//2):
            # n+1�N����ư��k�ɩ��W��, �u�bn�O�_�Ʈɦ��t
            # �|�ݭn���O�]���_��x�_�Ƥ�}��, �������������|��
            # Ex: 5x5�x�}�������|��, �n�Q�ץ��W�H�ά۹�����������90�B180�B270��2x3�x�}
            for j in range((n+1)//2):
                # �|�`�N��inplace���4�Ӥ����`�|�򥢤@�Ӥ�������
                # �ҥH��tmp�N��U�������s�U��, ������a�Mb�ȥ洫�ɭn���έ�tmp�Ȧs
                tmp = matrix[i][j]
                # ��90�ײ�i�C�|��i��, �Ӳ�n-1-j��|��j�C
                matrix[i][j] = matrix[n-1-j][i]
                # �쥻��n-1-i��|�ܦ�n-1-(n-1-i) = i�C
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

# By record matrix by deepcopy, time: O(n^2), space: O(n^2)
# inplace�ק諸�L�{�|�ॢ�쥻matrix������
# ���M�n�Dmatrix�����ninplace, ���S���w�L�k���B�~���Ŷ��ӰO��matrix���e
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         # �Q��python���O�����ܼ�, �ҥH�ba�O�}�C��, ��¥�b = a�|�b���a���P�ɧ��b
#         # copy.copy�O�L�ƻs, �@��ӻ����a���|�A���b, ���Y��ʨ�a��b���ѦҪ��ܼ�(�Ҧp�ĤG����list)���|�v�T
#         # ��copy.deepcopy�O�N��H�ѼƧ����ƻs�@����s���ܼƤU, �ҥH��̧����W�ߤ��|�v�T
#         # �o���H�ѼƬOmatrix, �ҥHtmp�]�O�@�ӤG���}�C
#         tmp = copy.deepcopy(matrix)
#         # ���Xtmp�Nmatrix���ܧ�
#         for i in range(n):
#             for j in range(n):
#                 # ����������90�פ����g�L�[��i�o
#                 # ��i��|���n-1-i�C, ��j�C�|���j��
#                 matrix[j][n-1-i] = tmp[i][j]
        
# @lc code=end

