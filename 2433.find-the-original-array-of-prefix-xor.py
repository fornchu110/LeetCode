#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
# By XOR, time: O(n), space: O(1)
# output分別每輪用頭1, 2, 3, 4, ...n個元素相XOR得到input
# 因XOR中1^0=1且1^1=0這種乘數和積交換的性質
# 相鄰input做xor即是答案, 用代換的來看
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # 先初始化res
        res = list()
        tmp = 0
        # 每輪讓pref[i-1]^pref[i], 即是答案
        # 用tmp的方式讓i可以不用range(1, len(pref)), 實作更快
        for i in pref:
            tmp ^= i
            res.append(tmp)
            # 重點在此, tmp每輪結束後要更新為這輪的i
            tmp = i
        return res
    
#  一樣意思不同寫法
#  class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         res = []
#         cur = 0
#         n = len(pref)
#         for i in range(n):
#             res.append(cur^pref[i])
#             cur ^= res[i]
#         return res
        
# @lc code=end

