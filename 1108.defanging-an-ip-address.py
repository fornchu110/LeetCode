#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
# By str.replace, time: O(n), space: O(1)
# �Q��str.replace�N�ؼЪ�.���N��[.]
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

        
# @lc code=end

