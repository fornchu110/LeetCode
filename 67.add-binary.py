#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = '', 0
        i, j = len(a)-1, len(b)-1
        while (i>=0 or j>=0 or carry):
            if i>=0:
                carry += int(a[i])
                i -= 1
            if j>=0:
                carry += int(b[j])
                j -= 1
            res = str(carry&1)+res
            carry //= 2
        return res

# class Solution:
#     def addBinary(self, a, b) -> str:
#         # int(a, 2)代表將a以二進制看求出十進制下的值並轉換成int
#         # Ex: a = 11, int(a, 2) = 3
#         x, y = int(a, 2), int(b, 2)
#         print(x, y)
#         while y:
#             # XOR可以做到2進制下的無進位相加結果
#             answer = x^y
#             carry = (x&y)<<1
#             x, y = answer, carry
#             print(x, y)
#         print(x, bin(x)[2:], bin(x))
#         return bin(x)[2:]
        
        
# @lc code=end

