#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
# 給一陣列nums, 要求找出陣列左半邊數總和等同右半邊數總和之index

# By enumerate, time: O(n), space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = 0
        for i in nums[1:]:
            r += i
        # 也可能以index0為界, 雖然l必為0, 但r剛好也是0, 畢竟元素有正有負
        if r==0:
            return 0
        # 注意不論如何切片, enumerate會從index0開始
        for idx, i in enumerate(nums[1:]):
            l += nums[idx]
            r -= nums[idx+1]
            if l==r:
                #因idx是從0開始, 而我實際在走訪的idx是從1開始
                return idx+1
        return -1
        
# @lc code=end

