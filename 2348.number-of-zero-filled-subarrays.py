#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
# 給一陣列nums, return裡面各種連續全為0的子陣列數目

# By DP, time: O(n), space: O(1)
# 子陣列數目要記得這招
# Ex: [0]只有1個子陣列, [0, 0]有3個子陣列, [0, 0, 0]有6個子陣列
# 所以會發現, 1 = 0+1, 3 = 1+2, 6 = 3+3, 每次發現新的0就+0的數量就是新增加的子陣列數目
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res

# @lc code=end

