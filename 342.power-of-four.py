<<<<<<< HEAD
#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# 給一個int n 如果他是4的冪, 那return True, 不然return False

# By bitwise and bin(n).count, time: O(logn), space: O(11 
# 利用bitwise技巧和bin(n).count來算1和0的數量並且根據4的冪的特性判斷
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4的冪一定是2的冪, 所以先判斷是不是2的冪
        # n&n-1消掉n最後中最後位的1, 2的冪只會有1個1, 所以消一次還非0代表非2的冪
        # 再來四的冪會有偶數個0, 但bin(n)回傳的是0b(n的二進制), 所以實際上會有奇數個0

        if n&n-1 or n<1 or not bin(n).count('0')&1:
            return False
        return True

# By bitwise(and mask), time: O(1), space: O(1)    
# 也可以用mask判斷, 因為4的冪之bit 1必定在奇數位上, 所以n&0x55555555==n才可能是4的冪
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and n&n-1==0 and n&0x55555555:
            return True
        else:
            return False
        
# By while, time: O(logn), space: O(1)
# time = O(logn)是因為0~4會判斷1次,5~16會判斷兩次... n = 4^(k-1)+1~4^k時會判斷k次 
# 用while暴力判斷
# class Solution:
#     def isPowerOfFour(self, n):
#         tmp = 0
#         while 4**tmp<= n:
#             if n==4**tmp:
#                 return True
#             tmp += 1
#         return False
    
# @lc code=end

=======
#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# 給一個int n 如果他是4的冪, 那return True, 不然return False

# By bitwise and bin(n).count, time: O(logn), space: O(11 
# 利用bitwise技巧和bin(n).count來算1和0的數量並且根據4的冪的特性判斷
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4的冪一定是2的冪, 所以先判斷是不是2的冪
        # n&n-1消掉n最後中最後位的1, 2的冪只會有1個1, 所以消一次還非0代表非2的冪
        # 再來四的冪會有偶數個0, 但bin(n)回傳的是0b(n的二進制), 所以實際上會有奇數個0

        if n&n-1 or n<1 or not bin(n).count('0')&1:
            return False
        return True

# By bitwise(and mask), time: O(1), space: O(1)    
# 也可以用mask判斷, 因為4的冪之bit 1必定在奇數位上, 所以n&0x55555555==n才可能是4的冪
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0 and n&n-1==0 and n&0x55555555:
            return True
        else:
            return False
        
# By while, time: O(logn), space: O(1)
# time = O(logn)是因為0~4會判斷1次,5~16會判斷兩次... n = 4^(k-1)+1~4^k時會判斷k次 
# 用while暴力判斷
# class Solution:
#     def isPowerOfFour(self, n):
#         tmp = 0
#         while 4**tmp<= n:
#             if n==4**tmp:
#                 return True
#             tmp += 1
#         return False
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
