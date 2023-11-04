#

# @lc app=leetcode id=1 lang=python3

#
# [1] Two Sum
#

# @lc code=start
# 給一陣列nums和整數target, 找出nums內兩兩和等同target之元素index

#By hashtable, time: O(n), space: O(n)
# 一邊走訪n一邊查找和建立hash, 當遇到target-自己的元素存在於hash代表找到res
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i in range(len(nums)):
            if target-nums[i] in hashtable:
                return [hashtable[target-nums[i]], i]
            hashtable[nums[i]] = i
        return []

#By for loop, time: O(n^2), space: O(1)
# 基本的做法, 雙迴圈兩兩比較
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if target-nums[i]==nums[j]:
#                     return [i, j]
#         return []

# @lc code=end

