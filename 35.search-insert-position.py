#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start

# By binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        min = 0
        max = n
        while(min<=max):
            # µ¥¦P©ó(min+max)//2
            mid = min+(max-min)//2
            if nums[mid]<target:
                min = mid+1
            else:
                max = mid-1
            print(min, max)
        return min

# @lc code=end

