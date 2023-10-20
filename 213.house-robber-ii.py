#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
# ���@�}�Cnums, �D�b�����۾F�����U�o��̤j�M�����k, �P198�D���t�O�b�o��nums�O��cycle
# �ҥH���]nums = [2, 0, 0, 2], �̤j�����k�O��nums[0]��nums[3] = 2, �����nums[0]+nums[3] = 4

# By DP, time: O(n), space: O(1)
# ���֤߷Q�k�Mcycle�@��, �t�O�b��nums[0]�Mnums[len(nums)-1]�u����䤤�@��
# �]�N�O��, �p��dp[0:len(nums)-1]�Mdp[1:len(nums)]��ر��p, ��̤j�����ӧY�i
# ��ꤣ�Ϊȵ��b�аO�Ĥ@���ЬO�_�Q��, �o�Ӱ��k��P�ɰ��Ĥ@���M�̫�@�����i��ʱư��Ӥw, �����Ҽ{�u���Ĥ@��, �Υu���̫�@��, �Ψⶡ���S��
# ��cycle���ӧǦC���ޥ��n�O�o
class Solution:
    # �ҥH�n��range�b[0:len(nums)-1]�ɥH��[1:len(nums)]�ɪ��̨θѰ����
    def rob(self, nums: List[int]) -> int:
        # �P198, ��̨θ�, �u�O���F�d�򰵭p��
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start+2, end+1):
                first, second = second, max(first + nums[i], second)
            return second
        length = len(nums)
        if length==1:
            return nums[0]
        elif length==2:
            return max(nums[0], nums[1])
        else:
            # ��ؽd�򪺳̨θѧ�j�����ӴN�O����
            return max(robRange(0, length-2), robRange(1, length-1))

        
# @lc code=end

