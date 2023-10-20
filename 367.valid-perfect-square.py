#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start

# By binary search, time: O(log(n)), space: O(1)
# 使用double pointer實作, 但重點精神是binary search
# 只切一半是O(n/2)也就是O(n), 要每輪都切一半才叫O(log(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = (left+right)//2
            square = mid*mid
            if square==num:
                return True
            elif square<num:
                left = mid+1
            else:
                right = mid-1
        return False

# @lc code=end

