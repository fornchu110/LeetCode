#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
# ���@�}�Cnums, �b����nums���۾F�����U, �o������̤j��

# By DP, time: O(n), space: O(1)
# ���dp[i]���ηQ������, �Q����i�Ӥ����U���̨θѧY�i
# �o��dp[1]�N�i��O��nums[0]��nums[1], ��dp[3]���αqdp[0]+nums[3]�H��dp[1]+nums[3]��, �]��dp[1]�ɴN�ӦҼ{��F
# �]���i�H�`�N��@�ӧ󪽱����ಾ��{, �u���W�w������۾F��, ����ڤWdp[i]�N�Omax(dp[i-2]+nums[i], dp[i-1])
# �B�̨θѥu��e��ӸѦ���, �ҥH�u�ݭn�Ψ�ΤT���ܼư����a�Y�i�٤U�Ŷ�
# �̫�return dp[len(nums)-1]�]�N�O�̷s��second
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, size):
            tmp  = second
            second = max(first+nums[i], second)
            first = tmp
            # ���ܼƼg�k, ��c����o�˦P�ɰ��B��
            # first, second = second, max(first + nums[i], second)
        return second

# By DP, time: O(n), space: O(n)
# �ۤv�g���@�k
# �o�D�n�`�N���N�O�p�󧹦�DP�ಾ��{, �쥻�H���u�n����_��index�����M�H�ΰ���index�����M
# ����ڤW���o��case, nums = [2, 0, 0, 2], �i�H�o�{��nums[0]+nums[3] = 4�~�O�̨θ�
# �[��X�L�׫���, �̫��Ӥ������w�|���@�ӳQ�飼, ���i��b�����諸���p���̨θ�(nums[i]��>0)
# �]���`�N��, ���]��dp[i]��@����nums[i]�ɪ��̨θ�, ��dp[i] = max(dp[i-3]+nums[i], dp[i-2]+nums[i])
# �̫�max(dp[len-1], dp[len-2])�N�O����
# �o�ӷQ�k�i��, ���t�פ���C�Ŷ��]�����h
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
#         elif len(nums)==2:
#             return max(nums[0], nums[1])
#         elif len(nums)==3:
#             return max((nums[0]+nums[2]), nums[1])
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         dp[2] = max(dp[0]+nums[2], dp[1])
#         for i in range(3, len(nums)):
#             dp[i] = max(dp[i-3]+nums[i], dp[i-2]+nums[i])
#         return max(dp[len(nums)-2], dp[len(nums)-1])
        
# @lc code=end

