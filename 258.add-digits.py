#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
# ���@�Ӽ�num, �N��U�Ӧ�Ƭۥ[, �Y�ۥ[�᪺���G�W�L�G��ƨ��N�~��, ����ѤU�@��Ƭ���

# By math, time: O(1), space: O(1)
# �μƾǪ���k�ҩ�, �άM�g���Q�k�h�Q
# �[���̫᪺���G�@�w�O0~9, �ҥH�n�Q��k��num�M�g��0~9
# �ӵo�{0�u���@�ر��p�N�O�@�}�l��0, �ҥH���Ӥ��}�Q��, ��ڤW�O�n�M�g��1~9
# %10���F�ҥH%9�ո�, ���o�{num%9�|�M�g��0~8, �n���L�M�g��0~9�ҥH��num%9+1
# ��num%9+1�S�|�o�{�b�Ӧ�ƿ��~, �ҥH��(num-1)%9+1
class Solution:
    def addDigits(self, num: int) -> int:
        # ��num��0, ���Mnum�@�ˬO9������, ���`�M���M�O0
        if num==0:
            return 0
        else:
            return (num-1)%9+1
        # �U���o�q���P�W��else����
        # # ��num�O9�����ƥB�D0��, �`�M�|�O9
        # elif num%9==0:
        #     return 9
        # # �_�h�`�M�|�Onum//9���l��, �]�N�Onum%9
        # else:
        #     return num%9

# By simulation, time: O(lognum), space: O(1)
# �Ψ�hwhile, �@�h�P�_num�O�_�W�L�G���, �W�L�G��ƴN�βĤG�hwhile�N�C�Ӧ�Ƭۥ[
# �o�ب��X�C�Ӧ�ƪ��ɶ������״N�Olognum
# class Solution:
#     def addDigits(self, num: int) -> int:
#         # ��num�O�G��ƴN�n���_��
#         while num>=10:
#             # �ۥ[�᪺���G
#             res = 0
#             # �Nnum�C��Ƭۥ[
#             while num:
#                 res += num%10
#                 num //= 10
#             # �̫�ۥ[�������G�ܦ��s��num
#             num = res
#         # num�Ѥ@�쨺�����N�O����
#         return num
    
# @lc code=end

