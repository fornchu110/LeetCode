<<<<<<< HEAD
#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start

# By inplace iterative, time: O(n), space: O(1)
# �C���n�[�W�e�X�����M
# ����DP�t���h, �N�e�X�����X�s�_�ӵ��U�@���[�W�h
# �ĤG�ӬO�h�ؤF�@��list, �����i�H��a�ק�
# �`�N��a�ק�Ψ�range���ӷ|��D��a�C
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# By iterative, time: O(n), space: O(1)
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         res = list()
#         tmp = 0
#         for i in nums:
#             res.append(i+tmp)
#             tmp = i+tmp
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start

# By inplace iterative, time: O(n), space: O(1)
# �C���n�[�W�e�X�����M
# ����DP�t���h, �N�e�X�����X�s�_�ӵ��U�@���[�W�h
# �ĤG�ӬO�h�ؤF�@��list, �����i�H��a�ק�
# �`�N��a�ק�Ψ�range���ӷ|��D��a�C
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# By iterative, time: O(n), space: O(1)
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         res = list()
#         tmp = 0
#         for i in nums:
#             res.append(i+tmp)
#             tmp = i+tmp
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
