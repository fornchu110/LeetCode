#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
# By string processing
# 璶盢num暗Ω6传Θ9, return硂巨程计
# 碞琌璶盢程蔼计6传Θ9, 硂贺眖オ程虏虫よ猭碞锣传Θstr
# string processing眖オ, 矪瞶Ч锣传Θint
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        # replace()琌肚Τэ跑筁, 1锣传1
        num = num.replace("6", "9", 1)
        return int(num)

# @lc code=end

