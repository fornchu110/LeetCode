#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
# 給字串s, return兩條成對'|'以外的'*'數量

# By simulation, time: O(n), space: O(1)
# 改良版, 一樣從頭走訪但只要符合條件時遇到'*'計數就好, 不用額外將其他字元放入tmp
class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        flag = 1
        for ch in s:
            # 在遇到"|"時做判斷, 因為flag只有0或1所以用not改變值就好
            if ch=='|':
                # 用not就不需要用if flag來判斷flag狀態, 反正遇到'|'就要更改flag
                flag = not flag
            # 當flag為1且是'*'時增加計數
            elif flag and ch=='*':
                res += 1
        return res    

# # By simulation, time: O(n), space: O(n)
# # 從頭走訪s, 將成對"|"之間以外的字元放入tmp, 再走訪tmp數"*"數量
# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         tmp = []
#         res = 0
#         # 利用flag知道目前是否在成對"|"中間, 也就是在遇到第一個"|"時將flag設為0
#         flag = 1
#         for ch in s:
#             if flag:
#                 tmp.append(ch)
#                 if ch=="|":
#                     flag = 0
#             else:
#                 if ch=="|":
#                     flag = 1
#         for ch in tmp:
#             if ch=="*":
#                 res += 1
#         return res
        
# @lc code=end

