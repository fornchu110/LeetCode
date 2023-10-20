#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# By binary search, time: O(log(n)), space: O(1)
# 只會找最多一半的可能性, 不會嘗試n個
class Solution:
    def guessNumber(self, n: int) -> int:
        min = 1
        max = n
        while(True):
            # 選擇只猜範圍的中間值
            # //2代表整數除法, 自動捨棄小數
            mid = (min+max)//2
            # 猜到答案, 直接return
            if(guess(mid)==0):
                return mid
            elif(guess(mid)<0):
                max = mid-1
            else:
                min = mid+1
        
# @lc code=end

