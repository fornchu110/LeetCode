#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start

# By double pointer, time: O(n), space: O(1)
# 以res不算空間複雜度的觀點是O(1), 不然res本身其實是O(n)
# 兩個pointer, 一開始指向0和指向n, 兩pointer必差距n個元素
# 這樣做n輪依序加入即可
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        odd = 0
        even = n
        while(n!=0):
            res.append(nums[odd])
            res.append(nums[even])
            odd += 1
            even += 1
            n -= 1
        return res

# By range, time: O(n), space: O(1)
# 省變數空間的作法, 但用到range時間較久
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         res = list()
#         for i in range(n):
#             res.append(nums[i])
#             res.append(nums[i+n])
#         return res
        
# @lc code=end

