#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start

# By enum , time: O(n), space: O(c), �]��26�ӭ^��r���ҥHc = 26
# �n�`�N��S�Ҩ��u���P�_, �T�{�n�S�Ҫ����p�A�}�l���B�z
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # ���פ��@�˥���false
        if len(s)!=len(goal):
            return False
        # �p�Gs�Mgoal�����ۦP, ���ӹ��o�˦b��ڥ洫�e�N�P�_, ���ө�b�᭱
        if s==goal:
            # ���ۦPchar����set���w����p, �i�H�洫
            if len(set(s))<len(goal): 
                return True
            # s�Mgoal���������S������char, ���i�洫
            else:
                return False
        # zip�b���N���Piterable��Ƶ��c���ۦP��m���⤸����i()��
        # �ҥHzip(s, goal)�O��list, zip(s, goal)[0] = (s[0], goal[0]), ...
        # ������u����Ƶ��c����, �˱���������ѤU������
        # zip���γ~�O�P�ɳB�z���Piterable��Ƶ��c, �ܾA�X�P�_str�O�_�ۦP�M�@�Psub str
        diff = [(a, b) for a, b in zip(s, goal) if a!=b]
        print(diff)
        # ��s�Mgoal�P��m�ɤ��Pchar�����p�ƶq, ���ӭn==2�B�洫��N�����۵�
        return len(diff)==2 and diff[0][0]==diff[1][1] and diff[0][1]==diff[1][0]

# @lc code=end

