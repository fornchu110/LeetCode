#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start

# By hash table, time: O(n), space: O(1)
# ノhash盢numsぇじ瞷Ω计癘魁ㄓ
# 芠诡安瞷3Ω, じぇgoodpair计1+2 = 3 = (3*2)/2
# 瞷4Ω, goodpair: 1+2+3 = 6 = (4*3)/2, 琌单畉计
# 单畉计そΑ: n*(n+1)/2
class Solution:
    # 璽砫单畉计, 璸衡赣じgoodpair计
    def arithmeticSequence(self, n):
        return (n*(n-1))//2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        hash = dict()
        # 盢じ瞷Ω计癘魁hashい
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # ǐ砐hashノ单畉计衡goodpairΩ计
        for i in hash:
            res += self.arithmeticSequence(hash[i])
        return res

# By for loop, time: O(n^2), space: O(1)
# 忌癹伴秆, 癸–じ常┕т筂皚goodpairΩ计
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         res = 0
#         # 常穦┕т, ┮ノrange
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 # 猔種ノrangei㎝j琌indexぃ琌numsぇじ
#                 # ノnums[i]㎝nums[j]ㄓ絋粄じ琌单
#                 if nums[i]==nums[j]:
#                     res += 1
#         return res

# @lc code=end

