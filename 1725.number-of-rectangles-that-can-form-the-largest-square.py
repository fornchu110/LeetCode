    #
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
# By math, time: O(1), space: O(1)
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res, max = 0, 0
        for a, b in rectangles:
            k = min(a, b)
            if k==max:
                res += 1
            elif k>max:
                res = 1
                max = k
        return res

# @lc code=end

