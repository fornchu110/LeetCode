#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
# ��X���w�x�}grid���C3x3���l�x�}�̳̤j�Ȩ�return

# By traversal(simulation), time: O(n^2), space: O(1)
# ���ΦC��ͦ���
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n =  len(grid)
        # ���ͦ�n-2��0���@���}�C, �A�N�o�Ӱ}�C�ͦ�n-2��
        # [0]*(n-2)�]�O�ͦ��@���}�C���@�k, ���G���@�w�n��for
        res = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                # �Q�ΦC��ͦ����ӱq�y��[i][j]�}�l��3*3�����X�ç�Xmax�]�w��res[i][j]
                res[i][j] = max(grid[x][y] for x in range(i, i+3) for y in range(j, j+3))
        return res

# @lc code=end

