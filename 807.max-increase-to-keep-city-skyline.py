#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
# By min()�Bmax() and index array, time: O(n^2), space: O(n)
# �]�o�D����ΩҥHO(n^2)
# ���h�ӫؿv������, �n�b���v�T�F��n�_�ݹL�h�ѻڽu���p�U�W�[�ؿv������
# �]�N�O����C�ӫؿv��, ��X�Prow�̰��M�Pcolumn�̰�, �W�[�ܸ��p�����䰪�קY�i
# ������j���ӬO�]������j���N�|�W�X�ѻڽu, ���p�~���|����
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # row���שMcol����, ��ڤW�o�D�]����Ϋؿv�����ҥHm=n
        m = len(grid)
        n = len(grid[0])
        rowmax = list()
        colmax = list()
        res = 0
        # �ΨӽT�{�W�[���׫᪺grid�Ϊ�, ��ڤW���ݭn
        # gridnew=[[0]*n for i in range(m)]
        # ��X�Crow�̤j��
        for i in grid:
            rowmax.append(max(i))
        # ��X�Ccol�̤j��, �`�N�Ocol�b�~�h, �]��n��col�̤j��
        for j in range(n):
            tmpmax = 0
            for i in grid:
                if i[j]>tmpmax:
                    tmpmax = i[j]
            colmax.append(tmpmax)
        # ��grid���C�ӫؿv��, ��X�L�Ҧbrow, col�̤j�Ȥ����p������
        for i in range(m):
            for j in range(n):
                # �T�{��
                # gridnew[i][j] = min(rowmax[i], colmax[j])
                res += min(rowmax[i], colmax[j])-grid[i][j]
        return res

# �x�谵�k, �@�˷N���²��ܦh, �t�פ����
# By map() and zip(), time: O(n^2), space: O(n)
# �Ƿ|max()�M�g�Mzip(*list)�N�}�C��m���@�k
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         # map()�O�N�}�C�����������w���, map(max, grid)�N�O��grid���Ҧ�������max()
#         # ���|��^�}�C, �n��list()�N�ܴ��������e�ഫ���}�C
#         # �o��o�˴N���P��X�Crow�̤j��
#         rowMax = list(map(max, grid))
#         # zip(*grid)���@�k�Q����m�x�}, �N��C����, �o�˦A��map()�K�O��Ccol�̤j��
#         # list(zip(grid))�|�bgrid�~�A�]�@�h
#         colMax = list(map(max, zip(*grid)))
#         return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))

# @lc code=end

