#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
# By XOR and <<, time: O(n), space: O(1)
# 以start為起點, 求每次都與start+2做XOR做n-1次的結果
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1, n):
            # i<<1代表i左移1位元, 等同於2*i
            # 注意位移優先權在+-*/下面, >=, ==...上面, 所以要括號
            res ^= start+(i<<1)
        return res
        
# @lc code=end

