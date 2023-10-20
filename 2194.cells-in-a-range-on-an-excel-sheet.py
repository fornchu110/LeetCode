#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
# By ord() and chr(), time: O(m*n), space: O(1), m��row��, n��column��
# ���_�I�M���I, �̧ǦL�X[�_�I, ���I]���Ҧ�����
# �@��col���X���A���X�U�@��
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        # ord()�Ψ���o�r�Ū�ascii�X
        # ��_�lascii�M���Iascii��for�j��, �Y�i�̧ǥ[�J�r��
        # �q�_�lcol�}�l
        for i in range(ord(s[0]), ord(s[3]) + 1):
            # �Pcol�U�q�_�lrow���X����Irow
            for j in range(ord(s[1]), ord(s[4]) + 1):
                # ��+�N�r�ųs���_��
                # chr��ascii��r��
                res.append(chr(i) + chr(j))
        return res

# @lc code=end

