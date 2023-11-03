#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
# ���@�ﳬ�϶���intervals�M�@�ӷs�϶�newInterval
# �u�nintervals���MnewInterval���|���϶��N�N�L�̦X��, �X�᪺֫�U�ɴN�O�o�ǰ϶��̤p�U��, �W���N�O�o�ǰ϶��̤j�W��
# return�����|���϶��M�X�ְ϶�, �o�ǰ϶��n�Ѥp��j�Ƨ�

# By simulation, time: O(n), space: O(1)
# ���I�b��p��P�_�U�Ӱ϶��O�_���MnewInterval���|
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # mer�N��X�ְ϶�
        mer = newInterval
        # ��flag�ӧP�_����ɭԭn�Ntmp�[�Jres
        flag = 1
        for i in intervals:
            # i[0]�N��϶��U��, i[1]�N��϶��W��, �U�ɥ��w<=�W��
            # ���X�쪺i���U�ɤ�newInterval���W���ٰ�, �N���i��PnewInterval���|
            # �B�o��i���᪺�U�ɪ֩w�]�󰪤��i�୫�|, �]���i�H�Nmer�[�Jres
            # �קKnerInterval�W�ɥ��ӴN��h��i���U���٧C�y�����ƥ[�J, �ҥH�ݭnflag
            if flag and i[0]>newInterval[1]:
                res.append(mer)
                # �Nmer�[�Jres�F, ���|�A�ݭn�[�J��L��
                flag = 0
            # ���I�b��, �u����ر��p�϶����MnewInterval���|
            # 1. �϶����W�ɤ�newIterval�U���٤p
            # 2.�϶����U�ɤ�newInterval�W���٤j
            if i[1]<min(newInterval) or i[0]>max(newInterval):
                res.append(i)
            # ��L���p���N��϶��MnewInterval�����|
            # ���N�ӬݬO�_�n��smer���W�U��
            # ���|���ܷs�U�ɴN�O���|�϶����U�ɳ̤p���U��, �s�W�ɴN�O���|�϶����W�ɳ̤j���W��
            # �o�䤣�ά�, ���p�G�O�n�ݭ��|���涰, ���涰�U�ɴN�O���|�϶����̤j���U��, �W�ɴN�O���|�϶����̤p���W��
            else:
                if i[0]<mer[0]:
                    mer[0] = i[0]
                if i[1]>mer[1]:
                    mer[1] = i[1]
        # flag��1�N���X��interval���S�Nmer�[�Jres, �ҥH�ɤW
        if flag:
            res.append(mer)
        # res�n�Ӱ϶��j�p�Ƨ�, ���U���o�˰��n���B�~�ɶ��ƧǤ��n
        # res.append(tmp)
        # res.sort()
        return res
        
# @lc code=end

