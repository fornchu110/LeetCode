<<<<<<< HEAD
#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
# ���}�Cintervals����h�ӥ��ƧǹL���϶�, �p�G�̭������|���϶��N�N��X��, return�B�z�������G

# By one by one compare, time: O(nlogn), space: O(logn)
# space = O(logn)��]�O�ƧǩҪ�O���Ŷ�������
# �Q���X�@���N�������w�n���ƧǹL, ��OO(nlogn)

# ��n�����k���ӬO��res���������ק�M���, �֧P�_�ĤG����ɱ���
# �]�|���H�U��sort�L�ҥH��ڤW�u�n�ݥH�Χ��W��
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # key = lamada�o�ӰѼƬOsort()���٤U�Ƨǹ�ڮɶ����n���ޥ�
        # �H�o�䬰��, �ڥu�Q���϶��ھڤU�ɰ��Ƨ�
        # �]��key = lambda x�N��̭��o�ǰ϶����Ox
        # ��x[0]�N�O�U��, �o�˴N���\���w�H�U�ɱƧ�, �Ӥ��﮳�X�B�z�W�ɪ�����
        # �p�G�O��list�����h��dict���Ƨ�, key�N�i�H���w�u�P�_����key��value���Ƨ�, �Ӥ��άݨ�L��
        # �ӥB�٥i�H��ܥH�h��key���P�_�u�O���P�u����, �o��p�G�[�J�W�ɧ@������
        # �N�n�g��: key = lambda x: x[0], x[1]
        # �P�ɥi�H����ʺA�p�����, ���ڦp�G�Q�H�W��-�U�ɪ��ȨӱƧǰ϶�
        # ���N�g��: key = lamda x: x[1]-x[0]
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # res�O�ũΥثe�϶����U�ɤ�res�̫�@�Ӱ϶����W�ɤj, �����N�϶��[�Jres
            # res[-1]�O�s���̫�@�Ӥ������ޥ�
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# �o��ڰ���
# �Q�k�q�Ĥ@�Ӥ����O���Xintervals�@�@����íק�intervals���۹������ʧ@
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []
#         intervals.sort(key = lambda x: x[0])
#         # ��ɱ���, ��u���@�Ӱ϶��N�i�H����return
#         if len(intervals)==1:
#             return intervals
#         for i in range(1, len(intervals)):
#             # �p�G��W�Ӱ϶��S�����|, �h��W�Ӱ϶��[�Jres
#             # �`�N�S�϶��S���|���P�w��k:�U��>�L���W�ɩΤW��<�L���U��, �����~�������|
#             if intervals[i][0]>intervals[i-1][1] or intervals[i][1]<intervals[i-1][0]:
#                 res.append(intervals[i-1])
#             # �p�G��W�Ӱ϶������|, �h��intervals���{�b���϶����W�U�ɧ令���|�᪺�϶�
#             else:
#                 intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
#                 intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
#             # ��ɱ���, ���X��̫�@�Ӱ϶���
#             # �p�G�O�S���|���p, ���F��W�Ӱ϶��[�Jres�~�]�n�N�ۨ��[�Jres
#             # �p�G�O���|���p, �b��粒�ۨ��϶��W�U�ɫ�]�n�N�ۨ��[�Jres
#             if i==len(intervals)-1:
#                 res.append(intervals[i])
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
# ���}�Cintervals����h�ӥ��ƧǹL���϶�, �p�G�̭������|���϶��N�N��X��, return�B�z�������G

# By one by one compare, time: O(nlogn), space: O(logn)
# space = O(logn)��]�O�ƧǩҪ�O���Ŷ�������
# �Q���X�@���N�������w�n���ƧǹL, ��OO(nlogn)

# ��n�����k���ӬO��res���������ק�M���, �֧P�_�ĤG����ɱ���
# �]�|���H�U��sort�L�ҥH��ڤW�u�n�ݥH�Χ��W��
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # key = lamada�o�ӰѼƬOsort()���٤U�Ƨǹ�ڮɶ����n���ޥ�
        # �H�o�䬰��, �ڥu�Q���϶��ھڤU�ɰ��Ƨ�
        # �]��key = lambda x�N��̭��o�ǰ϶����Ox
        # ��x[0]�N�O�U��, �o�˴N���\���w�H�U�ɱƧ�, �Ӥ��﮳�X�B�z�W�ɪ�����
        # �p�G�O��list�����h��dict���Ƨ�, key�N�i�H���w�u�P�_����key��value���Ƨ�, �Ӥ��άݨ�L��
        # �ӥB�٥i�H��ܥH�h��key���P�_�u�O���P�u����, �o��p�G�[�J�W�ɧ@������
        # �N�n�g��: key = lambda x: x[0], x[1]
        # �P�ɥi�H����ʺA�p�����, ���ڦp�G�Q�H�W��-�U�ɪ��ȨӱƧǰ϶�
        # ���N�g��: key = lamda x: x[1]-x[0]
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # res�O�ũΥثe�϶����U�ɤ�res�̫�@�Ӱ϶����W�ɤj, �����N�϶��[�Jres
            # res[-1]�O�s���̫�@�Ӥ������ޥ�
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# �o��ڰ���
# �Q�k�q�Ĥ@�Ӥ����O���Xintervals�@�@����íק�intervals���۹������ʧ@
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []
#         intervals.sort(key = lambda x: x[0])
#         # ��ɱ���, ��u���@�Ӱ϶��N�i�H����return
#         if len(intervals)==1:
#             return intervals
#         for i in range(1, len(intervals)):
#             # �p�G��W�Ӱ϶��S�����|, �h��W�Ӱ϶��[�Jres
#             # �`�N�S�϶��S���|���P�w��k:�U��>�L���W�ɩΤW��<�L���U��, �����~�������|
#             if intervals[i][0]>intervals[i-1][1] or intervals[i][1]<intervals[i-1][0]:
#                 res.append(intervals[i-1])
#             # �p�G��W�Ӱ϶������|, �h��intervals���{�b���϶����W�U�ɧ令���|�᪺�϶�
#             else:
#                 intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
#                 intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
#             # ��ɱ���, ���X��̫�@�Ӱ϶���
#             # �p�G�O�S���|���p, ���F��W�Ӱ϶��[�Jres�~�]�n�N�ۨ��[�Jres
#             # �p�G�O���|���p, �b��粒�ۨ��϶��W�U�ɫ�]�n�N�ۨ��[�Jres
#             if i==len(intervals)-1:
#                 res.append(intervals[i])
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
