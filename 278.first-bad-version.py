#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# By binary search, time: O(n), space: O(1)
# 左閉右閉寫法
class Solution:
    def firstBadVersion(self, n: int) -> int:
        min, max = 1, n
        while min<=max:
            mid = (max-min)//2+min
            if isBadVersion(mid):
                max = mid-1
            else:
                min = mid+1
        return min
        
# @lc code=end

