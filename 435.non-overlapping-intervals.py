#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
# ���@�}�Cintervals�����h�Ӱ϶�, �n�Dreturn�R���̤p�ư϶��ϳo�ǰ϶��������|
# �`�N�n�ھ��D���|�ҧP�_�϶��O�}�϶��٬O���϶�, ���e���h���϶�, ���o�D�O�}�϶�
# Ex: [1, 2], [2, 3]�èS�����|, �]�N�Onon-overlapping

# By greedy, time: O(nlogn), space: O(logn)
# space = O(logn)�O�]sort()�ҭn��O���Ŷ�
# �Q�k�O�N�϶��ھڤW�ɱƧ�, �ҥH���W�ɶV�C���϶��V������, �N�d����j���d����L�϶�
# �Y�n�@�϶��H�U�ɱƧǪ��g�k, �h�n�b���|���϶�����W�ɸ��C�̧@���d�U�Ӫ��϶�
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # ��ɱ���, ��intervals���S���϶�, �N���ΧR��return 0
        if len(intervals) == 0:
            return 0
        # ��key = lambda x: x[1]�ӮھڤW�ɱƧ�
        intervals.sort(key=lambda x: x[1])
        # cnt�������|���϶���, �b�ܤ֦��@�Ӱ϶������p�U��l��1
        cnt = 1
        # end�O�n������W��, ��l�Ƭ���0�Ӱ϶����W��
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # ��W�@�ӵ������϶��W��<=�ثe�϶����U��, �N���|���|
            if end <= intervals[i][0]:
                # �����|�϶���+1
                cnt += 1
                # �N�o�����϶��W�ɧ�s���������϶��W��, ���U�Ӱ϶����
                end = intervals[i][1]
        # �϶��`��-�����ư϶���=���ư϶���, �]�N�O�n�R�����϶��ƶq
        return len(intervals)-cnt

# @lc code=end

