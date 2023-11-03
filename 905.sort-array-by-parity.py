<<<<<<< HEAD
#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start

# By double pointer
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # �ؤ@��result, ���k�U�@��index
        idx1 = 0
        idx2 = len(nums)-1
        res = [0]*len(nums)
        # �Nnums�q�Y�ݨ��
        for i in range(len(nums)):
            # �p�G�ݨ참��, �q�����
            if(nums[i]%2==0):
                res[idx1] = nums[i]
                idx1 += 1
            # �p�G�ݨ�_��, �q�k���
            else:
                res[idx2] = nums[i]
                idx2 -= 1
        # �q�Y�ݧ��Bres�]��
        return res

# ��a�洫
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             while left < right and nums[left] % 2 == 0:
#                 left += 1
#             while left < right and nums[right] % 2 == 1:
#                 right -= 1
#             if left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1
#         return nums

# @lc code=end

=======
#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start

# By double pointer
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # �ؤ@��result, ���k�U�@��index
        idx1 = 0
        idx2 = len(nums)-1
        res = [0]*len(nums)
        # �Nnums�q�Y�ݨ��
        for i in range(len(nums)):
            # �p�G�ݨ참��, �q�����
            if(nums[i]%2==0):
                res[idx1] = nums[i]
                idx1 += 1
            # �p�G�ݨ�_��, �q�k���
            else:
                res[idx2] = nums[i]
                idx2 -= 1
        # �q�Y�ݧ��Bres�]��
        return res

# ��a�洫
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             while left < right and nums[left] % 2 == 0:
#                 left += 1
#             while left < right and nums[right] % 2 == 1:
#                 right -= 1
#             if left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1
#         return nums

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
