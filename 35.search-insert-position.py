#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start

# By binary search, time: O(logn), space: O(1)
# 注意有不同寫法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 左閉右開寫法, [min, max)
        min = 0
        max = len(nums)
        while(min<max):
            mid = (max-min)//2+min
            if nums[mid]<target:
                # 取整又是閉區間要+1
                min = mid+1
            else:
                max = mid
        return min
        # n = len(nums)-1
        # min = 0
        # max = n
        # # 左閉右閉寫法, [min, max]
        # while(min<=max):
        #     # 等同於(min+max)//2, 避免overflow
        #     mid = min+(max-min)//2
        #     if nums[mid]<target:
        #         min = mid+1
        #     else:
        #         max = mid-1
        #     print(min, max)
        # return min

# @lc code=end

