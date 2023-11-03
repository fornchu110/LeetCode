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
        # result, オindex
        idx1 = 0
        idx2 = len(nums)-1
        res = [0]*len(nums)
        # 盢nums眖繷Ю
        for i in range(len(nums)):
            # 狦案计, 眖オ娩
            if(nums[i]%2==0):
                res[idx1] = nums[i]
                idx1 += 1
            # 狦计, 眖娩
            else:
                res[idx2] = nums[i]
                idx2 -= 1
        # 眖繷ЧresЧ
        return res

# ユ传
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
        # result, オindex
        idx1 = 0
        idx2 = len(nums)-1
        res = [0]*len(nums)
        # 盢nums眖繷Ю
        for i in range(len(nums)):
            # 狦案计, 眖オ娩
            if(nums[i]%2==0):
                res[idx1] = nums[i]
                idx1 += 1
            # 狦计, 眖娩
            else:
                res[idx2] = nums[i]
                idx2 -= 1
        # 眖繷ЧresЧ
        return res

# ユ传
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
