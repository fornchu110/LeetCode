#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# By set, time: O(n), space: O(n)
# time: O(n)原因是將nums內容一一放入set也要O(n), 如果不算的話就O(1)
# python用set去除重複元素, 判斷set長度是否跟nums一樣即可知道是否有重複
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 有重複要True, 也就是兩者長度不同時會True, 所以用!=
        return len(nums)!=len(set(nums))

# By hash table, time: O(n), space: O(n)
# 如果給的nums內有重複元素就return True, 否則False
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash = dict()
#         for i in nums:
#             if i not in hash:
#                 hash[i] = 1
#             else:
#                 return True
#         return False

# By sort, time: O(n*log(n)), space: O(log(n))
# 有n個元素要排序所以time是O(n*log(n))
# 而sort()實際上是用遞迴, 所以space: O(log(n))便是sort()花費的空間複雜度
# 將nums先排序好, 判斷排序後的nums兩兩元素是否相等
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return True
#         return False
        
# @lc code=end

