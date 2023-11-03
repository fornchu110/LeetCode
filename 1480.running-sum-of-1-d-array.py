#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start

# By inplace iterative, time: O(n), space: O(1)
# 每項要加上前幾項之和
# 其實跟DP差不多, 將前幾項的合存起來給下一項加上去
# 第二個是多建了一個list, 但其實可以原地修改
# 注意原地修改用到range應該會比非原地慢
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

