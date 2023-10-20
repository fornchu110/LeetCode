#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def test(self, s):
        return s==s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s)
        while left<right:
            print(s[left:right])
            if self.test(s):
                return len(s)
            if s[left]!=s[right-1]:
                if self.test(s[left+1]):
                    left += 1
                else:
                    right -= 1
            print(left ,right)

# @lc code=end

