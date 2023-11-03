<<<<<<< HEAD
#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start

# By binary search, time: O(log(n)), space: O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1)//2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

# By iterative, time: O(n)
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         idx = 0
#         req = 0
#         while(True):
#             req += idx
#             if n==req:
#                 return idx
#             elif req>n:
#                 return idx-1
#             idx += 1

# @lc code=end

=======
#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start

# By binary search, time: O(log(n)), space: O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1)//2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

# By iterative, time: O(n)
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         idx = 0
#         req = 0
#         while(True):
#             req += idx
#             if n==req:
#                 return idx
#             elif req>n:
#                 return idx-1
#             idx += 1

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
