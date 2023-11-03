#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start

# By list, time: O(n), space: O(1) 
# space O(1)的原因是return之內容不算在空間複雜度
# 空間複雜度通常指return外用的額外空間
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = list()
        # python可以直接用i跑list內容, 會比用range更省記憶體
        # 這邊i就代表nums[i]
        for i in nums:
            ans.append(nums[i])
        return ans

# By inplace replacement, time: O(n), space: O(1)
# 時間換空間的作法, 原地修改nums不用額外空間
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         # 1000是因為題目說nums內容物範圍在[0, 999]
#         for i in range(n):
#             nums[i] += 1000*(nums[nums[i]]%1000) 
#         for i in range(n):
#             nums[i] //= 1000
#         return nums

# @lc code=end

