#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
# 要求找出nums內最大兩數-1後相乘的積

# By for and if-elif, time: O(n), space: O(1)
# 利用if和elif同時只會成立一個的方式做相應
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            if i>=a:
                b = a
                a = i
            elif i>=b:
                b = i
        return (a-1)*(b-1)
        
# @lc code=end

