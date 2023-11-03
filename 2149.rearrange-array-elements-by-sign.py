#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start

# 給一陣列nums, 要求依照元素正負正負重新排序, 且對同號數而言相對位置不能改變
# 題目有說正數和負數數量一樣, 所以必定做len(nums)/2輪

# By double pointer, time: O(n), space: O(1)
# 用兩個pointer紀錄目前正數和負數找到哪個index
# 每輪先找正數, 只要遇到負數就往下個找, 找到再加入res, 再來做負數同理
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = neg = 0
        res = list()
        for i in range(n//2):
            # 使用while使找到正數才結束
            while nums[pos]<0:
                pos += 1
            res.append(nums[pos])
            pos += 1
            # 使用while使找到負數才結束
            while nums[neg] > 0:
                neg += 1
            res.append(nums[neg])
            neg += 1
            # 每輪結束剛好加入一個正數一個負數進res, 共n/2輪
        return res

# By array, time: O(n), space: O(n)
# 走訪nums將依序將正負數存進pos和neg
# 最後再走訪len(nums)/2次, 每次依序將pos和neg內相同index的元素放進res
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = []
#         neg = []
#         res = []
#         for i in nums:
#             if i>0:
#                 pos.append(i)
#             else:
#                 neg.append(i)
#         for i in range(len(nums)//2):
#             res.append(pos[i])
#             res.append(neg[i])
#         return res
        
# @lc code=end

