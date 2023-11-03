#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

# By binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        min, max, res = 0, x, -1
        while min<=max:
            mid = (min+max)//2
            if mid*mid<=x:
                res = mid
                min = mid+1
            else:
                max = mid-1
        return res
        
# @lc code=end

