#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# 給一已排序陣列nums和target, 找出target在nums中第一次出現和最後一次出現的index

# By binary search, time: O(logn), space: O(1)
# 看到排序和找就要想到binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 注意bisec回傳的是插入點, 也就是說bisect會照排序return加入一個新的target進nums後他的index, 只是加入最左還是最右
        # Ex: [1, 2, 3]、t = 2, bisect_left(nums) = 1, 因為會變成[1, 2, 2, 3], bisect_right = 2
        # 所以在bisect_left得到的結果並無差別, 但bisect_right要-1
        r = bisect_right(nums, target)-1
        l = bisect_left(nums, target)
        # l跟r要在nums長度範圍內, 且nums[r]和nums[l]的確是查找的target
        if l<=r and r<len(nums) and nums[r]==target and nums[l]==target:
            return [l, r]
        # 否則代表找不到, 也就是[-1, -1]
        else:
            return [-1, -1] 

        
# @lc code=end

