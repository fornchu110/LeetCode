#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
# By XOR, time: O(n), space: O(1)
# output���O�C�����Y1, 2, 3, 4, ...n�Ӥ�����XOR�o��input
# �]XOR��1^0=1�B1^1=0�o�ح��ƩM�n�洫���ʽ�
# �۾Finput��xor�Y�O����, �ΥN�����Ӭ�
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # ����l��res
        res = list()
        tmp = 0
        # �C����pref[i-1]^pref[i], �Y�O����
        # ��tmp���覡��i�i�H����range(1, len(pref)), ��@���
        for i in pref:
            tmp ^= i
            res.append(tmp)
            # ���I�b��, tmp�C��������n��s���o����i
            tmp = i
        return res
        
# @lc code=end

