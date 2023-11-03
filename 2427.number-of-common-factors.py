#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
# 給a, b兩數, return a, b的公因數數量

# By simulation, time: O(min(a, b)), space: O(1)
# 優化1: 介於a, b之間的不可能是公因數, 因此只要迭代至min(a, b)以下的數
# 從1到min(a, b)測試a和b是否都整除, 也就是%0, 當成立時res+1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        if a>b:
            tar = b
        else:
            tar = a
        for i in range(1, tar+1):
            if a%i==0 and b%i==0:
                res += 1
        return res
        
# @lc code=end

