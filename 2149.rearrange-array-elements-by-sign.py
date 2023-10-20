#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start

# 倒皚nums, 璶―ㄌ酚じタ璽タ璽穝逼, 癸腹计τē癸竚ぃэ跑
# 肈ヘΤ弧タ计㎝璽计计秖妓, ┮ゲ﹚暗len(nums)/2近

# By double pointer, time: O(n), space: O(1)
# ノㄢpointer魁ヘ玡タ计㎝璽计тindex
# –近тタ计, 璶笿璽计碞┕т, тres, ㄓ暗璽计瞶
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = neg = 0
        res = list()
        for i in range(n//2):
            # ㄏノwhileㄏтタ计挡
            while nums[pos]<0:
                pos += 1
            res.append(nums[pos])
            pos += 1
            # ㄏノwhileㄏт璽计挡
            while nums[neg] > 0:
                neg += 1
            res.append(nums[neg])
            neg += 1
            # –近挡タ计璽计秈res, n/2近
        return res

# By array, time: O(n), space: O(n)
# ǐ砐nums盢ㄌ盢タ璽计秈pos㎝neg
# 程ǐ砐len(nums)/2Ω, –Ωㄌ盢pos㎝negずindexじ秈res
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

