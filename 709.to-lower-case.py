#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n = len(s)
# return小寫字串, 用lower()就能將字串大寫轉換成小寫
# 正常做應該是走訪s用ord()和chr()做ascii碼的轉換
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# By bitwise, time: O(n), space: O(1)
# |32是技巧, 大轉小剛好是ascii+32, 而32是2^5可以用|來達成大寫轉小寫
# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)

# @lc code=end

