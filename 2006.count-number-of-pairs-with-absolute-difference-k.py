#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
# 肚皚numsいindex i<j薄猵|nums[i]-nums[j]|==kpairs计秖

# By hash table, time: O(n), space: O(n)
# ノhash盢ǐ砐计ㄓ, 癘魁ヘ玡硂计ǐ砐碭
# –ǐ砐穝计, 碞琩穝计-k㎝穝计+kΤぶㄓ, 玡才|nums[i]-nums[j]|==k计ヘ
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hash = {}
        res = 0
        # –Ωǐ砐穝计龟悔讽nums[j], ǐ砐筁竒hash琌nums[i]
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            # 耞琌才|nums[i]-nums[j]|==k兵ン
            # 璶if in hash, 拨澈⊿﹍てhash穦тぃkey
            if i-k in hash:
                res += hash[i-k]
            if i+k in hash:
                res += hash[i+k]
        return res
        
# By double for loop, time: O(n^2), space: O(1)
# # ノ蛮癹伴ǐ砐
# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if abs(nums[i]-nums[j])==k:
#                     res += 1
#         return res
    
# @lc code=end

