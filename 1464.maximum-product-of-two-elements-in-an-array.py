#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
# �n�D��Xnums���̤j���-1��ۭ����n

# By for and if-elif, time: O(n), space: O(1)
# �Q��if�Melif�P�ɥu�|���ߤ@�Ӫ��覡������
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            if i>=a:
                b = a
                a = i
            elif i>=b:
                b = i
        return (a-1)*(b-1)
        
# @lc code=end

