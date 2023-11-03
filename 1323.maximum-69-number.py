#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
# By string processing
# 要將num做一次6換成9, return這操作最大的數
# 就是要將最高位數的6換成9, 這種從左看到右最簡單的方法就先轉換成str
# 因為string processing從左到右看, 處理完再轉換成int
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        # replace()是回傳值才有改變過, 1代表只轉換1個
        num = num.replace("6", "9", 1)
        return int(num)

# @lc code=end

