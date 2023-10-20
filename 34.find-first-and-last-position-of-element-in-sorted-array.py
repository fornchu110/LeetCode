#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r = bisect_right(nums, target)-1
        l = bisect_left(nums, target)
        print(l, r)
        if l<=r and r<len(nums) and nums[r]==target and nums[l]==target:
            return [l, r]
        else:
            return [-1, -1] 

        
# @lc code=end

