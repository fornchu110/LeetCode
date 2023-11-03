#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
# �n�D�X�̤j�n���l�ƦC
# �`�N�n���l�ƦC�u�n���W>1���ƥB�t�Ƭ����ƭ�, ���@�w�ܤֶV���V�j
# �J��0�~�ݭn���m

# By count negtive, time: O(n), space: O(n)
# �|�y�L��DP�٧֤@��
# ���ƭӭt�ƪ��ܶV���V�j, �_�ƭӭt�ƪ���, �C�ӭt�ƥ��k����l�ƦC�@�w�����ƭӭt��
# ���઺�ηN�O�]��ӼƦC����l�ƦC, �]���̪��l�ƦC����Onums[:len(nums)]��nums[1:len(nums)-1]�_�@
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # reversed(nums)�i�H�Nnums����æ^���|�N��, �n��list����
        # �O������ٯ��nums.reverse()���^��, �H��nums[::-1]�����覡
        reverse_nums = list(reversed(nums))
        # �N����᪺nums���Xrange(1, len(nums))���P��쥻nums[:len(nums)-1]
        # �i�H�o�˰��O�]�����k���ǬۤϤ��|�v�T���G
        # �U���Τ@��for�j��P�ɨ��X���list
        for i in range(1, len(nums)):
            # or���ت��O���F��J��nums[i-1]��0��, �ﭼ�W1
            # �Ʋ�or�B��b�����D0�ɪ�������, ������0�ɤ~�ݥk��, and�B�⥪����0�ɪ�������, �����D0�~�ݥk��
            # �קKnums[i-1]=0����nums[i]�]�ܦ�0, ���@���P�qnums[i]���s�}�l
            # �`�N�ޥ��O��nums�Mreverse_nums�s�W�F���X��i�ɪ��ۭ����G
            # �ҥH�̫��max()���P���C�جۭ����G�̭��̤j��, �o�X����
            nums[i] *= nums[i-1] or 1
            reverse_nums[i] *= reverse_nums[i-1] or 1
        # +�O�N��list���������@��list, ���|���������ۥ[
        # Ex: a = [1, 2], b = [3, 4], a+b = [1, 2, 3, 4]
        return max(nums+reverse_nums)

# By DP, time: O(n), space: O(1)
# DP�P�ɦҼ{min�Mmax����]�O, ��min�u�n�A�J��@�ӭt�ƴN�i���ܦ�max
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 
#         res = nums[0]
#         pre_max = nums[0]
#         pre_min = nums[0]
#         # nums[1:]���g�k�i�H����range�]�qindex��1����m���X, �Bnum���N��nums[index]
#         for num in nums[1:]:
#             cur_max = max(pre_max*num, pre_min*num, num)
#             cur_min = min(pre_max*num, pre_min*num, num)
#             res = max(res, cur_max)
#             pre_max = cur_max
#             pre_min = cur_min
#         return res

# @lc code=end

