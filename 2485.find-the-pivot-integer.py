#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
# 給n, 找出從1~n中, 是否有數res, 其1+...+res==res+...+n

# By math, time: O(1), space:O(1)
# 先求出1+..+n總和, 再將兩條件相等時的條件做代數運算, 實際上就是當x*x==m在x為整數時有解
# 這題還可以用二分搜尋法, 基本上能用平方根解決的都能用二分搜尋法解決
class Solution:
    def pivotInteger(self, n: int) -> int:
        m = n*(n+1)//2
        x = int(m**0.5)
        if x*x==m:
            return x
        else:
            return -1

# By for loop optimization, time: O(n), space: O(1)
# 最基本的作法是暴力解, 兩個迴圈
# 發現其實可以先求1+..+n, 每次只透過+-運算來求出1+..+res和res+..+n
# 不需要都再做乘法運算res*(res+1)/2來求出1+..+res這個等差數列, 加法和減法更快速
# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         #1+..+res可以用每輪+i的方式更新
#         tmp1 = 0
#         # res+...+n可以用每輪-(i-1)的方式更新
#         tmp2 = n*(n+1)//2
#         for i in range(1, n+1):
#             tmp1 += i
#             tmp2 -= i-1
#             if tmp1==tmp2:
#                 return i
#         return -1
        
# @lc code=end

