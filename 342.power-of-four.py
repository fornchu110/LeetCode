#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# 給一個int n 如果他是4的冪, 那return True, 不然return False

# By bitwise and bin(n).count, time: O(logn), space: O1 
# 利用bitwise技巧和bin(n).count來算1和0的數量並且根據4的冪的特性判斷
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4的冪一定是2的冪, 所以先判斷是不是2的冪
        # n&n-1消掉n最後中最後位的1, 2的冪只會有1個1, 所以消一次還非0代表非2的冪
        # 再來四的冪會有偶數個0, 但bin(n)回傳的是0b(n的二進制), 所以實際上會有奇數個0
        if n&n-1 or n<1 or not bin(n).count('0')&1:
            return False
        return True
# @lc code=end

