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
# �u�|��̦h�@�b���i���, ���|����n��
class Solution:
    def guessNumber(self, n: int) -> int:
        min = 1
        max = n
        while(True):
            # ��ܥu�q�d�򪺤�����
            # //2�N���ư��k, �۰ʱ˱�p��
            mid = (min+max)//2
            # �q�쵪��, ����return
            if(guess(mid)==0):
                return mid
            elif(guess(mid)<0):
                max = mid-1
            else:
                min = mid+1
        
# @lc code=end

