#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
# 回傳陣列nums中在index i<j的情況下|nums[i]-nums[j]|==k的pairs數量

# By hash table, time: O(n), space: O(n)
# 利用hash將走訪到的數字存下來, 並且記錄目前這個數字走訪到了幾個
# 每走訪到新數字, 就去查新數字-k和新數字+k有多少加上來, 代表前面符合|nums[i]-nums[j]|==k的數目
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hash = {}
        res = 0
        # 每次走訪到的新數字實際上當作nums[j]在看, 走訪過已經在hash上的是nums[i]
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            # 判斷是否符合|nums[i]-nums[j]|==k的條件
            # 要if in hash才可以, 畢竟沒初始化hash可能會找不到key
            if i-k in hash:
                res += hash[i-k]
            if i+k in hash:
                res += hash[i+k]
        return res
        
# By double for loop, time: O(n^2), space: O(1)
# # 用雙重迴圈走訪
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if abs(nums[i]-nums[j])==k:
#                     res += 1
#         return res
    
# @lc code=end

