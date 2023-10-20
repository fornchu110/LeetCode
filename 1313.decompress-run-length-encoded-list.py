#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
# By extend and 2 step range, time: O(n+m), space: O(1), m是freq總和
# O(n+m)中+m的原因是每次要再插入 m個val
# 用extend比用用append快速
# 一對一對看, index偶數時為freq, 下一個是val, 將val插入freq次
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = list()
        # 可以直接用range(0, len(nums, 2))來只在index為偶數時做事
        # 照理來說range(0, len(nums), 2)只看一半個n, 複雜度沒變但應該比較快
        for i in range(0, len(nums), 2):
            # 或是range(len(nums)
            # 然後用if i&1==0來判斷i是偶數時, 比i%2==0快
            # 原本的作法, 使用append
            # freq = nums[i]
            # val = nums[i+1]
            # for j in range(freq):
            #     res.append(val)
            # 使用extend在res後面直接接上新list, 比append快
            # 有freq個val所以寫為val*freq, 通常被乘數表示價值, 乘數表示數量
            res.extend([nums[i+1]]*nums[i])
        return res

# @lc code=end

