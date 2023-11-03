<<<<<<< HEAD
#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
# By greedy, time: O(1), space: O(1), ��������sort()�����W�[�ɶ�������
# �n�N���wnum�C��Ʃ�������, �ç�X�Ҧ�����զX����ƩM�̤p�����өM
# �`�Ninput�O1000~9999, �ҥH�u�|���|���, �|��Ʃ��Ө��Ƴ̦n(�`�M�̤p)
# ����p����Ӧ�Ʃ���ƪ��̦��, ���j�����Ʃ���ƪ��Ӧ�� 
class Solution:
    def minimumSum(self, num: int) -> int:
        # �s����
        digits = list()
        # �Ninput���C�Ӧ�Ʃ�ilist
        while num:
            digits.append(num%10)
            num //= 10
        # �g�Lsort�K�o�����p�M���j����ƬO����, sort()�Ѥp��j
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end

=======
#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
# By greedy, time: O(1), space: O(1), ��������sort()�����W�[�ɶ�������
# �n�N���wnum�C��Ʃ�������, �ç�X�Ҧ�����զX����ƩM�̤p�����өM
# �`�Ninput�O1000~9999, �ҥH�u�|���|���, �|��Ʃ��Ө��Ƴ̦n(�`�M�̤p)
# ����p����Ӧ�Ʃ���ƪ��̦��, ���j�����Ʃ���ƪ��Ӧ�� 
class Solution:
    def minimumSum(self, num: int) -> int:
        # �s����
        digits = list()
        # �Ninput���C�Ӧ�Ʃ�ilist
        while num:
            digits.append(num%10)
            num //= 10
        # �g�Lsort�K�o�����p�M���j����ƬO����, sort()�Ѥp��j
        digits.sort()
        return 10*(digits[0]+digits[1])+digits[2]+digits[3]

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
