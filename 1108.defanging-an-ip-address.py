#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
# By str.replace, time: O(n), space: O(1)
# 利用str.replace將目標的.替代成[.]
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

        
# @lc code=end

