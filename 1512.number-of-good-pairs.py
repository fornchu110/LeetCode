#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start

# By hash table, time: O(n), space: O(1)
# 先用hash將nums之元素的出現次數記錄下來
# 觀察到假如出現3次, 此元素之goodpair數為1+2 = 3 = (3*2)/2
# 出現4次, goodpair: 1+2+3 = 6 = (4*3)/2, 是等差數列
# 等差數列公式: n*(n+1)/2
class Solution:
    # 負責等差數列, 計算該元素的goodpair數
    def arithmeticSequence(self, n):
        return (n*(n-1))//2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        hash = dict()
        # 將元素出現次數記錄在hash中
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # 走訪hash利用等差數列算出goodpair次數
        for i in hash:
            res += self.arithmeticSequence(hash[i])
        return res

# By for loop, time: O(n^2), space: O(1)
# 暴力迴圈解, 對每個元素都往後找遍陣列看goodpair次數
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         res = 0
#         # 因為都只會往後找, 所以用range
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 # 注意用range後i和j只是index不是nums之元素
#                 # 用nums[i]和nums[j]來確認元素是否相等
#                 if nums[i]==nums[j]:
#                     res += 1
#         return res

# @lc code=end

