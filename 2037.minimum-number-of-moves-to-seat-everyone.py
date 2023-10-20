#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
# ���@�}�Cseats�Mstudents, seats[i]�Mstudents[i]�N���i�Ӫ���m
# �@���u�ಾ��student�@�Ӧ�m, �ݱN�Ҧ�student�U���t��@��seat���̤p���ʦ���
# �@�}�l�]�i��|���h��student�b�P�Ӧ�m

# By sort, time: O(nlogn), space: O(logn), space = O(logn)�O�ƧǩҪ�O��stack�Ŷ�
# �Nseats�Mstudent���ƧǹL��@�@�۴�Y�i
# �ƧǩҥN���O�N�ǥͲ��ʨ����ۤv�̪񪺦�m
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        # ��zip�P�ɨ��X��Ӥ��P�}�C���ۦPindex������, i�Bj���O�N���Uindex�b�Ӱ}�C������
        for i, j in zip(seats, students):
            res += abs(i-j)
        return res

# @lc code=end

