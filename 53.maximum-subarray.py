#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# By dynamic programming, time: O(n), space: O(1)
# 找出最大子陣列和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = 0
        # 注意一開始要有個最大和, 避免只有一個元素時的狀況
        res = nums[0]
        # 比較正確的想法
        # 看過去和與當下元素i哪個大, 大者當新和
        # 得到新和後, 比較新和與最大和哪個大, 大者當最大和
        for i in nums:
            if tmp+i<i:
                tmp = i
            else:
                tmp = tmp+i
            if tmp>res:
                res = tmp
        # 我自己的做法
        # 看過去和+當下元素是否>0, 若<0代表要用下個>0元素當新和
        # for i in nums:
        #     if tmp+i<0:
        #         tmp = 0
        #         # 重點, 就算過去和+當下元素<0, 當下元素也可能比最大和還大
        #         if i>res:
        #             res = i
        #         continue
        #     else:
        #         tmp += i
        #         # 過去和+當下元素>0就繼續+, 若>最大和則成為最大和
        #         if tmp>res:
        #             res = tmp
        return res
        
        
# @lc code=end

