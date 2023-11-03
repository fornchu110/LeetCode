#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
# ��mxn����l�Ưx�}�M�@�}�Cindices, indices���C�@��[ri�Bci]�N��N��ri�C�H�β�ci��Ҧ�����+1
# �̫�return�x�}�����h��odd
# By simulation, time: O(q*(m+n)+m*n), space: O(m*n), �䤤q = len(indices)
# �����D�ذ����Ʊ�, ���Xindices�N���w����C�@�ӭ�+1, �̫�A�Ưx�}����odd��
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res = 0
        arr = [[0 for i in range(n)] for j in range(m)]
        # ���Xindices�Ҧ�����
        # q*(m+n)������, �O������ת�+�O�N������j������
        for [r, c] in indices:
            # r�N���r�C��n�Ӥ����n+1
            for i in range(n):
                arr[r][i] += 1
            # c�N���c�檺m�Ӥ����n+1
            for i in range(m):
                arr[i][c] += 1
        # �Ƶ��G
        # m*n������
        for i in range(m):
            for j in range(n):
                if arr[i][j]%2:
                    res += 1
        return res
    
        
# @lc code=end 

