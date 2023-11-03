#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# 給一個數要求得出其二進位下1的個數

# By bitwise, time: O(log(n)), space: O(1), n為給定數中1的各數
# 技巧在於利用n&(n-1)會把最低位元的1轉換成0的性質, 要記得這招
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

# By bitwise, time: O(k), space: O(1), 因題目給32位元數所以k = 32
# 從最右邊開始每次和1做&, 若最右邊那位是1那結果就是1, 然後右移循環數
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             if n&1:
#                 res += 1
#             n >>= 1
#         return res
        
# @lc code=end
