#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# By hash table, time: O(m+n), space: O(m), m琌jewles, n琌stones
# 璶jewelsず才jewelsず瞷碭Ω
# 盢jewelsず甧ǐ砐Ωhash table, ǐ砐ΩstoneΩ计
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # setpython琌hast table贺, ぃ穦Τ狡じ
        # ノadd㎝remove, ぃ钩listノappend
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                res += 1
        return res

# By for loop, time: O(m*n), space: O(1), m琌jewles, n琌stones
# 璶jewelsず才jewelsず瞷碭Ω
# 硂贺糶猭–Ωǐ砐stonesず甧常jewelsǐ砐筂, ┮琌m*n
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         res = 0
#         for i in stones:
#             if i in jewels:
#                 res += 1
#         return res

# @lc code=end

