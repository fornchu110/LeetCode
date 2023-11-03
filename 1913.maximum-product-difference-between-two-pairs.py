#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
# 給一個nums, 要求用裡面四個index不同的元素a, b, c, d求出a*b-c*d為最大值

# By greedy, time: O(n), space: O(1)
# 因只是單純找出最大2個和最小兩個元素, 直接走訪不排序也找得出來
# 但python實作上比sotred()還慢, 可能是資料量太少
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化最大兩值
        mx1, mx2 = max(nums[0], nums[1]), min(nums[0], nums[1])
        # 初始化最小兩值
        mn1, mn2 = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, n):
            tmp = nums[i]
            if tmp>mx1:
                mx1, mx2 = tmp, mx1
            elif tmp>mx2:
                mx2 = tmp
            if tmp<mn1:
                mn1, mn2 = tmp, mn1
            elif tmp<mn2:
                mn2 = tmp
        return (mx1*mx2)-(mn1*mn2)

# 這種題目最簡單就是先排序過, 找最大兩元素和最小兩元素
# By sorted(), time: O(n*log(n)), space: O(n)
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         sort = sorted(nums)
#         n = len(sort)
#         res = sort[n-1]*sort[n-2]-sort[1]*sort[0]
#         return res

# @lc code=end

