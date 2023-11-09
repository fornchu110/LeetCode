#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

# @lc code=start
# 給一字串s, return s中字元完全相同的子字串出現多少次
# 答案數字太大的話要%(10**9+7)

# By math, time: O(n), space: O(1)
# 不用迴圈計算出現次數, 而是一邊走訪到字元就算出出現次數
# Ex: 1個字元出現1次, 是連續的第2個字元就多出現2次, 連續的第三個字元就多出現三次
# 一邊走訪就一邊計算而不是等找出子字串再從頭算, 有點DP的味道
class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        # l和r分別代表一個子字串的開頭跟結尾
        l = 0
        for r, char in enumerate(s):
            if char==s[l]:
                # 長度為2子字串就多出現2-1+1 = 2
                # 如果下個仍一樣變成長度為3, 多出現3-1+1 = 3
                res += r-l+1
            else:
                # 新的字元重置r並出現1次
                l = r
                res += 1

        return res %(10**9+7)


# By math, time: O(n!), space: O(1), n = len(s)
# 暴力法, 長度為3的子字串全部出現次數是1+2+3 = 6, 長度為2就是1+2
# 所以走訪s, 每次碰到跟上個字元不同的字元代表完成一個新的子字串(元素完全相同)
# 把這個子字串長度送去計算出現次數即可
# class Solution:
#     def __init__(self):
#         self.res = 0

#     def count(self, n):
#         tmp = 0
#         while(n):
#             tmp += n
#             n -= 1
#         return tmp

#     def countHomogenous(self, s: str) -> int:
#         n = len(s)
#         tmp = 1
#         # 注意由於是跟前一個比對, 因此走完時最後一組子字串沒算到
#         # 要多做一輪把最後一組子字串的出現次數算出來加入res
#         for i in range(1, n+1):
#             if(i==n):
#                 self.res += self.count(tmp)
#                 break
#             if s[i]==s[i-1]:
#                 tmp += 1
#             else:
#                 self.res += self.count(tmp)
#                 tmp = 1
#         return self.res%(10**9+7)
    
# @lc code=end

