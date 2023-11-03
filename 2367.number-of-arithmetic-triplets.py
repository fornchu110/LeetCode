#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
# By hash, time: O(n), space: O(n)
# 給diff和nums, 找nums內有幾對(i, i+diff, i+diff)存在
# 用hash即可, 這種只要把所有input放進表且無關重複的可以直接用set()
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        hash = dict()
        for i in nums:
            if i not in hash:
                hash[i] = i
            if i-diff in hash and i-diff-diff in hash:
                res += 1
        return res 

# By three pointer, time: O(n), space: O(1)
# 因nums已經排序, 所以可以用pointer當作題目給的i、j
# 想法是走訪nums內所有元素, 先找到比x小diff的元素所在index j, 再找比x小2*diff的元素所在index i
# 當找到就代表有一對要求的組合
# class Solution:
#     def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
#         # j從index 1開始是因為三元素index不能重複, (i, j, x)至少要是(0, 1, 2)
#         res, i, j = 0, 0, 1
#         for x in nums:
#             # 隨著走訪nums, j會增加避免了重複組合
#             while nums[j]+diff<x:
#                 j += 1
#             # 邊界條件處理, 
#             if nums[j]+diff>x:
#                 continue
#             while nums[i]+diff*2<x:
#                 i += 1
#             if nums[i]+diff*2==x:
#                 res += 1
#         return res

# @lc code=end

