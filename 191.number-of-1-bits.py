<<<<<<< HEAD
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# 倒计璶―眔ㄤ秈1计

# By bitwise, time: O(log(n)), space: O(1), n倒﹚计い1计
# мォノn&(n-1)穦р程じ1锣传Θ0┦借, 璶癘眔硂┷
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

# By bitwise, time: O(k), space: O(1), 肈ヘ倒32じ计┮k = 32
# 眖程娩秨﹍–Ω㎝1暗&, 璝程娩ê琌1ê挡狦碞琌1, 礛簿碻吏计
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             if n&1:
#                 res += 1
#             n >>= 1
#         return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# 倒计璶―眔ㄤ秈1计

# By bitwise, time: O(log(n)), space: O(1), n倒﹚计い1计
# мォノn&(n-1)穦р程じ1锣传Θ0┦借, 璶癘眔硂┷
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

# By bitwise, time: O(k), space: O(1), 肈ヘ倒32じ计┮k = 32
# 眖程娩秨﹍–Ω㎝1暗&, 璝程娩ê琌1ê挡狦碞琌1, 礛簿碻吏计
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             if n&1:
#                 res += 1
#             n >>= 1
#         return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
