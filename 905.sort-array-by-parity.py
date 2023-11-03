#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start

# By double pointer
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 建一個result, 左右各一個index
        idx1 = 0
        idx2 = len(nums)-1
        res = [0]*len(nums)
        # 將nums從頭看到尾
        for i in range(len(nums)):
            # 如果看到偶數, 從左邊放
            if(nums[i]%2==0):
                res[idx1] = nums[i]
                idx1 += 1
            # 如果看到奇數, 從右邊放
            else:
                res[idx2] = nums[i]
                idx2 -= 1
        # 從頭看完且res也放完
        return res

# 原地交換
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

